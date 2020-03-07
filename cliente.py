#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Programa Cliente
 
import socket
import sys

def recortarnombre(fila):
	nombre = ''
	ret = ''
	for i in fila[::-1]:
		if(((ord(i) != 92) and (ord(i) != 47))):  
			nombre += i
		else:
			break
	for j in nombre[::-1]:
		ret += j
			
	return ret 

tamBloque = 4096

# Escribimos direccion servidor , puerto y fichero a enviar
servidor = str(raw_input('Escribe la direccion del server a enviar fichero.\n'))
puerto = int(raw_input('Escribe el puerto habilitado por el servidor.\n'))
fila = str(raw_input('Escribe ruta y fichero a enviar.\n'))

# Creando el socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Conecta el socket en el puerto cuando el servidor estÃ© escuchando
server_address = (servidor , puerto)
print (sys.stderr, 'conectando a %s en el puerto %s' % server_address)
sock.connect(server_address)
print("Conectado a "+ str(servidor))
try:
	infile = open( fila , 'rb')
	message = infile.read()
	infile.close()
	#hay que quedarse solo con el nombre del fichero en la cadena fila
	nombre = recortarnombre(fila)
	print('El fichero a enviar es ' + nombre)
	# Enviando datos
	# primero enviamos el nombre del fichero
	sock.send(nombre.encode('UTF-8'))
	# Ahora enviamos el fichero
	sock.sendall(message)
except:
	print('Hubo un fallo al enviar el fichero....saliendo.')

finally:
    print (sys.stderr, 'cerrando socket')
    sock.close()
