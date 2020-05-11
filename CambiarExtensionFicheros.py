import os
from os import listdir
from os.path import isfile, isdir

def ls1(path):    
    return [obj for obj in listdir(path) if isfile(path + obj)]



lista = ls1('C:/Users/Pedro/OneDrive/Documentos/Python/pruebas/')
for old in lista:
	new = old
	new = new.replace("jpg","png")
	os.rename('C:/Users/Pedro/OneDrive/Documentos/Python/pruebas/'+ old,
		'C:/Users/Pedro/OneDrive/Documentos/Python/pruebas/' + new)



