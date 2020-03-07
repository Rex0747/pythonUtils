# -*- coding: utf-8 -*-
 
# Programa Servidor
# www.pythondiario.com
 
import socket
import sys
 
tamBloque = 4096
ruta = raw_input('Introduce ruta a donde descargar el fichero\n')
# Creando el socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Enlace de socket y puerto
server_address = ('192.168.1.3', 1111)
print (sys.stderr, 'empezando a levantar %s puerto %s' % server_address)
sock.bind(server_address)

# Escuchando conexiones entrantes
sock.listen(5)
data = 'a'
datos = ''
errores = False
nombre= ''
try:
	while data:
		# Esperando conexion
		print (sys.stderr, 'Esperando para conectarse')
		connection, client_address = sock.accept()
		# primero cogemos nombre del fichero
		nombre = connection.recv(50)
		print('Nombre de fichero ' + nombre)
    
		print (sys.stderr, 'Conexion realizada desde', client_address)
		# Recibe los datos en trozos y reetransmite
		while True:
			data = connection.recv(tamBloque)
			datos += data
			#print >>sys.stderr, 'recibido "%s"' % data
			if data:
				#print('Quedan datos')
				data = ''
            
				#print >>sys.stderr, 'enviando mensaje de vuelta al cliente'
				#connection.sendall('ok\n')
			else:
				print('Descarga finalizada.')
				print('Escribiendo fichero ' + nombre)
				print('Espere....')
				#print >>sys.stderr, 'no hay mas datos', client_address
				break
except:
	print('Hubo un error al recibir el fichero')
	errores = True
	
finally:
	#cerramos la conexion
	connection.close()
	if(errores == True):
		 exit
	else:
		fila = open( ruta + str(nombre) ,'w')
		fila.write(datos)
		fila.close()
		print('Fichero bajado correctamente.')

#print(datos)
