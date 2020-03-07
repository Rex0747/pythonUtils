# -*- coding: UTF-8 -*-
from suds.client import Client
import os
import Crypto
from Crypto.Cipher import AES
from Crypto import Random
import sqlite3 as lite
import sys
import time
from openpyxl import load_workbook
from imp import reload
reload(sys)  # Reload does the trick!
#sys.setdefaultencoding('UTF-8')

key = b'Pelikano_0747_oO'
iv = Crypto.Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CFB, iv)
msg = iv + cipher.encrypt(b'Attack at dawn')   #cifrado
#print(msg)

#msg = "CREATE TABLE gfhs (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,codigo VARCHAR(5) NOT NULL,nombre VARCHAR(50) NOT NULL)"
#msg = "INSERT INTO gfhs (codigo , nombre)VALUES ('HPSQU','PSQUIATRIA')"
msg = "SELECT * FROM articulos where id < 10"
#msg = "UPDATE gfhs SET codigo = 'HMGEN' WHERE id = 1"
#msghex = ':'.join(x.encode('hex') for x in msg) #pasar msg a hex
#print(msghex)
#msgstr = msg.format(0x0F) #msg.format(0x0F)
#print(msgstr)                         #pasar a string el hex
lista = ""
l = len(msg)

for i in msg:
    lista += str(ord(i)) + ','
    
#lista[:1] + lista[(l+1):]
#print(lista)

cl = Client('http://192.168.1.34:7789/?wsdl')
cl.options.cache.clear()
#consulta = msghex.format(0x0F)              #RetornarConsultaHex
res = cl.service.RetornarConsultaHex(lista)  #ExecCommandHex
#res = cl.service.ExecCommandHex(lista)
#print(res)
print(len(res))
n = 0
for i in res:
    #print(type(i))
    for j in i:
        #print[j[n] + "   " + str(n)]
        #print(type(j))
        print(len(j))
        for k in j:
            #print(type(k))
            print(k.encode('utf-8') + " id= " + str(n))
            n += 1
print(sys.stdout.encoding)
    



