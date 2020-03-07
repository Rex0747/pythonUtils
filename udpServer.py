import socket

UDP_IP = "192.168.1.11"
UDP_PORT = 5481
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(256) # buffer size is 1024 bytes
    print("Recibido de Arduino:", data )
    print( addr )
    #sock.sendto( " Repuesta desde server " ,(192.168.1.40 , 5480));
