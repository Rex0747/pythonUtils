# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 23:22:23 2020

@author: Pedro
"""

import platform
import json

sistema = platform.system()
print(sistema)

lista = [['H8NA', 'IZL020'], ['H8NA', 'IZ020'], ['H8NB', 'IZL025'], ['H8NB', 'IZ026'], ['H8NC', 'IZ010']]
bloque = '['

for i in lista:
    #bloque += '{"gfh": "%s","nombre": "%s" ' %( mtx[0],mtx[1])
    bloque += '{"gfh": "%s","nombre": "%s"},' %( i[0], i[1])
res = bloque[ :-1] + "]"

print(res)

j = json.loads(res)
print(j)
print(type(j[0]))
k = json.dumps(j)
print(type(k))
print(k)

from hashlib import blake2b
passw = "Hola"
h = blake2b(digest_size=25)
h.update( passw.encode() )
passwd = h.hexdigest()
print(passwd)


