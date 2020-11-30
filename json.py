# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:48:05 2020

@author: Pedro
"""

import json


confx ="""  
[       {
          "modulo": "",
          "estanteria": "", 
          "ubicacion": "",
          "division": 0,
          "codigo": "" ,
          "pacto" : 0,
          "gfh" : "",
          "dispositivo": "",
          "hopital" : ""
        },
        {
          "modulo": "",
          "estanteria": "", 
          "ubicacion": "",
          "division": 0,
          "codigo": "",
          "pacto" : 0,
          "gfh" : "",
          "dispositivo": "",
          "hopital" : ""
         }         ]

             """
             
bloque = """
        {
          "modulo": "",
          "estanteria": "", 
          "ubicacion": "",
          "division": 0,
          "codigo": "",
          "pacto" : 0,
          "gfh" : "",
          "dispositivo": "",
          "hospital" : ""
     
         """  
mtx = (('2','4','7','1','98988','20.0','H7NA','IZ034','HCSC'),('3','1','2','1','011334','1.0','H7NA','IZL024','HCSC'))

print(len(mtx))

jeiso = '['
j = 0
for i in range(len(mtx)):
    
    if j < len(mtx) -1:
        jeiso += bloque + '},'
        j += 1
    else:
        jeiso += bloque + '}'
                

jeiso += ']'
#print(jeiso)
v = json.loads(jeiso)


j= 0
for i in v:
    
    i['modulo'] = mtx[j][0]
    i['estanteria'] = mtx[j][1]
    i['ubicacion'] = mtx[j][2]
    i['division'] = mtx[j][3]
    i['codigo'] = mtx[j][4]
    i['pacto'] = mtx[j][5]
    i['gfh'] = mtx[j][6]
    i['dispositivo'] = mtx[j][7]
    i['hospital'] = mtx[j][8]

    j += 1
    
jeiso = json.dumps(v)
print(jeiso)
print(type(jeiso))










