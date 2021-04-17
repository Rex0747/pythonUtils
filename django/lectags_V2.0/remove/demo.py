import signal
import re
import array
import fcntl
import struct
import termios
import os
import sys
import subprocess
import traceback

class PyKeyUpKeyDown(object):
  def __init__(self):
    #  All of the following constants are defined in
    #  the Linux kernel: include/uapi/linux/kd.h
    self.KDGKBMODE = 0x4B44  #  Get current keyboard mode
    self.KDSKBMODE = 0x4B45  #  Set current keyboard mode
    self.KDGKBTYPE = 0x4B33  #  Get current keyboard type
    self.K_MEDIUMRAW = 0x02  #  Medium raw (keycode) mode

    #  Operational variables for this class:
    self.original_mode = None
    self.old_attr = None
    self.fd = None
    self.done = False
    signal.signal(signal.SIGINT, self.shutdown)
    signal.signal(signal.SIGHUP, self.shutdown)
    signal.signal(signal.SIGQUIT, self.shutdown)
    signal.signal(signal.SIGILL, self.shutdown)

    rtn = self.setup_keylisten()
    if rtn:
      print("Successfully set up keylistener.  Press Ctrl+c to exit.")
      while not self.done:
        e = self.get_next_key_event()
        self.on_key_event(e)
    else:
      print("Was unable to set up keylistener.  Perhaps you need to use 'sudo'?")
    self.cleanup()

  def on_key_event(self, e):
    if e is not None:
      print("Observed %s for keycode=%u" % ("keyup" if e['is_up'] else "Keydown", e['keycode']))

  def shutdown(self, signum, frame):
    print("Caught signal %s. Shutting down." % (str(signum)))
    self.done = True

  def has_a_keyboard(self, f):
    #  Looking inside the linux kernel in include/uapi/linux/kd.h,
    #  it looks like the kernel defines all of
    #  KB_84      0x01
    #  KB_101     0x02
    #  KB_OTHER   0x03
    #  as potential return values of ioctl -> tty3270_ioctl -> kbd_ioctl, for self.KDGKBTYPE
    #  however, only KB_101 is ever returned anywhere...
    #  Therefore, if this ioctl doesn't trigger an exception, assume
    #  that it is associated with an underlying keyboard.
    try:
      buf = array.array('i', [0])
      fcntl.ioctl(f, self.KDGKBTYPE, buf, 1)
      return True
    except:
      return False

  def identify_keyboard_sources(self, a):
    rtn = {}
    for x in a:
      rtn[x] = {}
      f = None
      try:
        f = os.open(x, os.O_RDONLY, 0)
        rtn[x]['has_keyboard'] = self.has_a_keyboard(f)
        rtn[x]['exception_on_open'] = False
      except Exception as e:
        rtn[x]['has_keyboard'] = False
        rtn[x]['exception_on_open'] = str(e)
      if f is not None:
        os.close(f)
    return rtn

  def cleanup(self):
      if self.original_mode is not None:
        if self.fd:
          fcntl.ioctl(self.fd, self.KDSKBMODE, self.original_mode)
      if self.old_attr is not None:
        if self.fd:
          termios.tcsetattr(self.fd, 0, self.old_attr)
      if self.fd is not None:
        if self.fd:
          os.close(self.fd)
        self.fd = None

  def modeset(self):
    #  These file paths sourced from getfd.c (See 'showkey' Linux tool source code.)
    sources = self.identify_keyboard_sources(["/dev/tty", "/dev/tty0", "/dev/console", "/dev/vc/0"])

    self.fd = None
    for source in sources:
      if sources[source]['has_keyboard']:
        self.fd = os.open(source, os.O_RDONLY, 0)
        break

    if self.fd == None:
      sys.stdout.write("No keyboard device could be identified.  Perhaps you forgot to use 'sudo'?\n")
      sys.exit(1)

    #  Query to determine the current keyboard mode so we can restore it later.
    buf = array.array('i', [0])
    fcntl.ioctl(self.fd, self.KDGKBMODE, buf, True)
    self.original_mode = buf[0]

    #  Save terminal parameters to restore them later.
    self.old_attr = termios.tcgetattr(self.fd)
    self.new_attr = termios.tcgetattr(self.fd)

    #  See comments and code in cpython/Modules/termios.c on method
    #  'termios_tcgetattr(PyObject *self, PyObject *args)' of python standard library implementation.
    #  in Modules/termios.c
    self.new_attr[0] = 0 # iflag
    #  self.new_attr[1] is oflags.
    #  self.new_attr[2] is cflags.
    #  Turn off canonical mode, turn of character echo, turn on control character signals.
    self.new_attr[3] = ((self.new_attr[3] & ~termios.ICANON & ~termios.ECHO) | termios.ISIG) # lflags
    #  self.new_attr[4] is ispeed.
    #  self.new_attr[5] is ospeed.
    #  See http://www.unixwiz.net/techtips/termios-vmin-vtime.html for
    #  details on VMIN and VTIME.  Curent values give blocking reads for maximum responsiveness:
    self.new_attr[6][termios.VMIN] = 1
    self.new_attr[6][termios.VTIME] = 0

    #  Apply the terminal mode changes:
    termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_attr)
    fcntl.ioctl(self.fd, self.KDSKBMODE, self.K_MEDIUMRAW)

  def get_keyboard_file_descriptor(self):
    return self.fd

  def get_next_key_event(self):
    try:
      if self.fd:
        buf = bytearray(os.read(self.fd, 1))
        return self.key_process(buf)
      else:
        return None
    except Exception as e:
      return None

  def key_process(self, buf):
    i_c = 0
    while i_c < len(buf):
      s = (buf[i_c+0] & 0x80)

      #  This calculation is implemented in showkey.c of the kdb package.
      #  I think it has a dependency on having at least a 2.6 kernel.
      if i_c + 2 < len(buf) and (buf[i_c+0] & 0x7f) == 0 and (buf[i_c+1] & 0x80 != 0) and (buf[i_c+2] & 0x80 != 0):
        kc = (buf[i_c+1] & 0x7f) << 7 | (buf[i_c+2] & 0x7f)
        i_c += 3
      else:
        kc = (buf[i_c] & 0x7f)
        i_c += 1

    return {
      'keycode': kc,
      'is_up': bool(s)
    }

  def setup_keylisten(self):
    try:
      self.modeset()
    except Exception as e:
      traceback.print_exc()
      sys.stdout.write("An exception happend when while listening to keycodes: " + str(e) + ".\n")
      return False
    return True

a = PyKeyUpKeyDown()