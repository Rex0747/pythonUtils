#! /home/pi/Python/lectags/env/bin/python3.7
# -*- coding: utf-8 -*-

import signal
import keyboard
import time
import json



class MyKeyEventClass1(object):
  
  def __init__(self):
    self.done = False
    self.txt = ''
    signal.signal(signal.SIGINT, self.cleanup)
    keyboard.hook(self.my_on_key_event)
    while not self.done:
      time.sleep(1)  #  Wait for Ctrl+C

  def cleanup(self, signum, frame):
    self.done = True
    print('cleanup')

  def my_on_key_event(self, e):
    k = e.to_json()
    #key = json.loads(k)
    #print(str(key))
    tecla = e.name #key['name']
    ev = e.event_type #key['event_type']
    #code = key['scan_code']
    #bfila = open('/home/pi/Python/lectags/lec.log','a+')
    if ev == 'down':
        if tecla != 'enter':
           keyboard.press('shift')
           print(keyboard.write("Python Programming is always fun!"))
            
        else:
            keyboard.send('Fin')
            
    #fila.close()
    
    
# f = open('/home/pi/Python/lectags/ini.log','a')
# f.write('Inicio aplicion correctamente.')
# f.close()   

a = MyKeyEventClass1()