# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:07:41 2020

@author: Pedro

modulo        = 0
estanteria    = 1
ubicacion	  = 2
division      = 3
codigo	      = 4
nombre        = 5
pacto         = 6
minimo	      = 7
dc            = 8
gfh           = 9
disp          = 10
hosp          = 11

"""
from excell import Excell
from excell import campos

xlsx = Excell('AMBU.xlsx')
#print(type(xlsx))
#fila = xlsx.leer_fichero2()
#print(type(fila))
#print(fila)

# cmps = None
lista = xlsx.leer_fichero2()
# for row in xlsx.leer_fichero2():

    

for cmps in lista:
    print(cmps.modulo)
    print(cmps.estanteria)
    print(cmps.ubicacion)
    print(cmps.division)
    print(cmps.codigo)
    print(cmps.nombre)
    print(cmps.pacto)
    print(cmps.minimo)
    print(cmps.dc)
    print(cmps.gfh)
    print(cmps.dispositivo)
    print(cmps.hospital)






