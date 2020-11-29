# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:48:05 2020

@author: Pedro
"""

import json


confx ="""  
[{
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
        }]

             """

v = json.loads(confx)
#print(v)

print(type(v))

for i in v:
    i['modulo'] = '2'
    i['estanteria'] = '5'
    i['ubicacion'] = '6'
    i['division'] = '2'
    i['pacto'] = '2'

print(v)










