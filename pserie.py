# -*- coding: UTF-8 -*-
import serial
import sys
from time import sleep

#print(ser.portstr)      # check which port was really used
#ser.write("hello")      # write a string
lista = [];

ip="192.168.1.40";mascara="255.255.255.0";penlace="192.168.1.1";dns1="8.8.8.8";dns2="8.8.4.4";
dispositivo="BURZUM";mac="12:17:13:23:33:44";sport="5480";dport="5481";ip_1="192.168.1.3";ip_2="192.168.1.34";ip_3="192.168.1.39";mode="0"
lista.append(ip)
lista.append(mascara)
lista.append(penlace)
lista.append(dns1)
lista.append(dns2)
lista.append(mac)
lista.append(ip_1)
lista.append(ip_2)
lista.append(ip_3)
lista.append(sport)
lista.append(dport)
lista.append(dispositivo)
lista.append(mode)




# while len(ip) < 6 :
# 	ip = raw_input("Introduce la ip del dispositivo\n")               #0
# 	lista.append(ip)
# while len(mascara) < 6 :
# 	mascara = raw_input("Introduce la mascara del dispositivo\n")     #1
# 	lista.append(mascara)
# while len(penlace) < 6 :
# 	penlace = raw_input("Introduce la gateway del dispositivo\n")      #2
# 	lista.append(penlace)
# while len(dns1) < 6 :
# 	dns1 = raw_input("Introduce la dns1 del dispositivo\n")            #3
# 	lista.append(dns1)
# while len(dns2) < 6 :
# 	dns2 = raw_input("Introduce la dns2 del dispositivo\n")            #4
# 	lista.append(dns2)
# while len(dispositivo) < 6 :
# 	dispositivo = raw_input("Introduce el nombre del dispositivo\n")   #5
# 	lista.append(dispositivo)
# while len(mac) < 6 :
# 	mac = raw_input("Introduce la mac del dispositivo\n")              #6
# 	lista.append(mac)
# sys.stdin.flush()
# while int(sport) < 1024 or int(sport) > 64000 :
# 	sport = raw_input("Introduce puerto origen del dispositivo\n")     #7
# 	lista.append(sport)
# sys.stdin.flush()
# while int(dport) < 1024 or int(dport) > 64000 :
# 	dport = raw_input("Introduce puerto destino del dispositivo\n")     #8
# 	lista.append(dport)
# while len(ip_1) < 6 :
# 	ip_1 = raw_input("Introduce la ip del Servidor 1\n")                #9
# 	lista.append(ip_1)
# while len(ip_2) < 6 :
# 	ip_2 = raw_input("Introduce la ip del Servidor 2\n")                #10
# 	lista.append(ip_2)
# while len(ip) < 6 :
# 	ip_3 = raw_input("Introduce la ip del Servidor 3\n")                #11
# 	lista.append(ip_3)



print("Se va a enviar los siguientes datos a " + dispositivo+ " , Pulsa 1 para enviar , 0 para cancelar.")
print("-IP: " + str(lista[0]))
print("-MASCARA: " + str(lista[1]))
print("-PENLACE: " + str(lista[2]))
print("-DNS1: " + str(lista[3]))
print("-DNS2: " + str(lista[4]))
print("-MAC: " + str(lista[5]))
print("-IP_SERVER1:" + str(lista[6]))
print("-IP_SERVER2:" + str(lista[7]))
print("-IP_SERVER3:" + str(lista[8]))
print("-PUERTO ORG: " + str(lista[9]))
print("-PUERTO DESTINO: " + str(lista[10]))
print("-NOMBRE: " + str(lista[11]))
print("-NODO: " + str(lista[12]))
#res = raw_input("Pulsa Tecla para enviar datos.")
#print(res)
res = ""
puerto = "COM3"
ser = serial.Serial( puerto , baudrate = 1200, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE,stopbits = serial.STOPBITS_ONE , timeout = 2 )  # open first serial port

for i in range(1):
	#ser.write("CONF".encode() + '\n'.encode())
        ser.write("Z\n".encode() )
        sleep(0.3)
        res = ser.readline()
        print( "Mode operacion: " + res )

for j in range(1):
	if( res != "0"):
		print("Debe imprimir la lista.")
		for itm in lista:
			#ser.write(str(itm).encode() + "\n".encode())
			ser.write(str(itm).encode() + '\n' )
			print("Se envio " + str(itm))
			#print(" Se recibio ".encode() + ser.readline() )
			print(" Se recibio " + ser.readline() )


print("Se enviaron datos de configuracion al puerto " + puerto )
#for i in range(12):
#	ser.write( lista[i] )


ser.close()  
#raw_input("Teclea para salir")

#import serial.tools.list_ports as port_list
#ports = list(port_list.comports())
#for p in ports: 
#	print (p)
