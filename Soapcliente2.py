# -*- coding: UTF-8 -*-
from suds.client import Client
import os
import sys
cl = Client('http://192.168.1.34:7789/?wsdl')
cl.options.cache.clear()
cl.service.EnviarFichero()
cl.service.getnombre('netscan.exe')

res = cl.service.RetornarConsulta('SELECT * FROM usuarios where id > 900')
print(res)
