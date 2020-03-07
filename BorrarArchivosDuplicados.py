#!/usr/bin/python
# -*- coding: utf-8 -*-                                      
												                          
import sys												           
import os                                          
from os import listdir                            
from os.path import isfile, join                    
from os import walk, getcwd 
from Crypto.Hash import SHA256
import collections    
            

											
def dir(ruta = '.'):  #Lista carpeta completa incluidos diectorios
    return listdir(ruta)
 
def ls(ruta = '.'):   #listar solo ficheros
    return [arch for arch in listdir(ruta) if isfile(join(ruta, arch))]  
    
def ls2(ruta = getcwd()):#Lista directorios y subdirectorios
    listaarchivos = []
    for (_, _, archivos) in walk(ruta):
        listaarchivos.extend(archivos)
    return listaarchivos
    
def RetArrayNombreTamano(ruta): #retorna una tupla con nombre y tamaoño de cada fichero
	FileArray = []
	File = []
	contenido = ls(ruta)
	i = 0
	for fichero in contenido:
		File = [ fichero , os.stat(ruta + fichero).st_size]
		FileArray.append(File)
		i += 1
	return FileArray
	
def RetNumeFicheDire(ruta):
	i = 0 #iterator
	lista = RetArrayNombreTamano(ruta)
	for fila in lista:
		i += 1
	return i

def CompararTamanos(ruta):
	i = 0 #iterator
	lista = RetArrayNombreTamano(ruta)
	tmp = []
	tmp2 = []
	tmphash = []
	for fila in lista:
		for f in lista[i:]:
			if((FileArray[i][0] != f[0]) and (FileArray[i][1] == f[1]) and FileArray[i][0] not in ArrayRepetidos  and  FileArray[i][1] not in ArrayRepetidos): 
				tmp.append(f[0])
		i += 1
	for ind in tmp:
		#print('tmp  ', ind)
		if( ind not in ArrayRepetidos):
			ArrayRepetidos.append(ind)
		
	#numrep = len(ArrayRepetidos)
	#numfichrep = len(ArrayRepetidos)
	for item in ArrayRepetidos:
		filetmp = LeerFichero(ruta + item)
		hashtmp = generarHash(filetmp)
		ficheror = ruta + item
		tmp2 = [ficheror , hashtmp]
		tmphash.append(tmp2)
	#print(ArrayRepetidos)
	#print [x for x, y in collections.Counter(hashtmp).items() if y > 1]
	#for i in tmphash:
		#print(i)
	return tmphash
        


def generarHash(fichero):
	m = SHA256.new()
	m.update(fichero)
	return m.hexdigest()

def LeerFichero(fichero):
	infile = open(fichero , 'rb')
	data = infile.read()
	infile.close()
	return data			
  
ArrayRepetidos = [] 
#file_status_array = os.stat('/home/peli/SqliteData.s3db')  #entrega las propiedades de un fichero
#print(file_status_array.st_size)
ruta = 'J:/BackupWhatsspp/videos/' #'/media/usb0/videos/' #'/home/peli/Downloads/'
numficheros = str(RetNumeFicheDire(ruta))
print('El numero de ficheros es de ' + numficheros)
FileArray = RetArrayNombreTamano(ruta)
duplicados = CompararTamanos(ruta)
numfichrep = len(ArrayRepetidos)
if(numfichrep == 0):
	print("No hay ficheros duplicados")
	raise SystemExit(1)
	
print('El numero de ficheros con el mismo tamaño es de '+ str(numfichrep))

print('ATENCION TODOS ESTOS FICHEROS SERAN BORRADOS DE SU DISCO...')
for i in duplicados:
	pass #print(i)
retorno = raw_input('Quieres borrarlos para toda la puta vida....? , Si / No\n')
if(retorno == 'Si'):
	i = 0
	#En la lista de duplicados tenenos el nombre del fichero y el hash , se necesita una funcion que mantenga la primera fila y borre el resto.
	for x in duplicados:
		os.remove(x[0])
		i += 1
	print('Se han eliminado ' , i , ' archivos.')
else:
	exit()	

#tupla = ls2('/home/peli/Downloads')
#for i in tupla:
#	if (i[0] != '.'):
		
#		print(i)
	
	
	
#st_size: tamaño en bytes.
#st_mode: tipo de archivo y bits de permisos.
#st_ino: número de inodo.
#st_dev: identificador del dispositivo.
#st_uid: identificador del usuario propietario.
#st_gid: identificador del grupo propietario.
#st_atime: fecha-hora del último acceso (en segundos).
#st_mtime: fecha-hora de la última modificación (en segundos).
#st_ctime: fecha-hora ultimo cambio (unix) o creación (win).
#st_atime_ns, st_mtime_ns y st_ctime_ns (idem. expresado en nanoseg).
#st_blocks: número de bloques de 512 bytes asignados.
#st_blksize: tamaño de bloque preferido por sistema.
#st_rdev: tipo de dispositivo si un dispositivo inode.
#st_flags: banderas definidas por usuario.
#st_gen: Número fichero generado.
#st_birthtime: tiempo de creación del archivo.
#st_rsize: tamaño real del archivo.
#st_creator: creador del archivo.
#st_type: tipo de archivo.
#st_file_attributes: atributos. 

