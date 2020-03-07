#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 11/2/2017

@author: peli
'''
#import socket
import sys
import os
import base64
from os import listdir 
import soaplib
from soaplib.core.service import rpc, DefinitionBase , soap 
from soaplib.core.model.primitive import String, Integer
from soaplib.core.server import wsgi
from soaplib.core.model.clazz import Array
from soaplib.core.model.primitive import Float
from soaplib.core.model.primitive import Boolean
from soaplib.core.model.primitive import Any
from soaplib.core.model.clazz import ClassModel
import sqlite3
import sqlite3 as lite
from Crypto.Hash import SHA256
from Crypto.Cipher import AES                           
from os.path import isfile, join
from pygeocoder import Geocoder
import serial
import pyowm

import RPi.GPIO as GPIO
import time


reload(sys)  # Reload does the trick!
sys.setdefaultencoding('utf-8')

servidor = '192.168.1.34'
puerto = 7789


class lista_(ClassModel):
	__namespace__ = "punk.tunk"
	numero = String #Integer
	calle =String
	pais = String
	codigo = String
	
class Funciones(DefinitionBase):
    @soap(String,_returns = String)
    def hashc(self , tx):
        print(tx)
        m = SHA256.new()
        if(tx == None):
            tx = 'Esta funcion parece no funcionar.pasa de todo.'
            return tx
        m.update(tx)
        return m.hexdigest()
    
    @soap(String,Integer,_returns=Array(String))
    def say_hello(self,name,times):
        results = []
        for i in range(0,times):
            results.append('Hello, %s'%name)
        return results

    @soap(Integer , Integer,_returns=Integer)
    def suma(self, a, b):
        return a + b

    @soap(String ,_returns=String)
    def ConvMay(self , txt):
        ret = ''
        for i in txt:
            car = ord(i) -32
            ret += chr(car)
        return ret
    
    @soap(String , _returns=Array(String))
    def devt(self , txt):
        txt += txt
        
        return txt
    
    @soap(String,returns=Array(String))
    def _dir(self,ruta = '.' ):
        if(ruta == None):
            ruta = '/home/peli/'
        #return (arch for arch in listdir(ruta) if isfile(join(ruta, arch)))
        return os.walk(ruta)
    
    @soap(String,_returns=String)   #@soap(String,_returns = Array(String))
    def get_datos(self,consulta):
        return 'Funciono ' + consulta
        
	
	@soap(String,_returns=String)
	def hextostr(txt):
		return txt.format(0x0F)
    
class Database(DefinitionBase):
	@soap(String,_returns=Array(String))
	def RetornarConsulta(self, consulta ):
		print(consulta)
		lista = []
		tmp = []
		conn = lite.connect("/home/peli/SqliteDbs/SqliteData.s3db")
		if(conn is  None): 
			print("No se abrio base de datos")
		curs=conn.cursor()
		curs.execute(str(consulta).encode('UTF-8'))
		for row in curs.fetchall():
			#print(row)
			tmp.append(str(row).encode('utf-8'))
			
		for ix in tmp:
			lista.append(str(ix).encode('utf-8'))
			#print(ix)
		tmp = []
			
		for j in lista:
			tmp.append(str(j).encode('UTF-8'))
		conn.close()
		return tmp
		
	@soap(String,_returns=Array(String))
	def RetornarConsultaHex(self, elem ):
		txtspl = elem.split(',')
		del txtspl[len(txtspl) - 1]
		sql = ''
		for i in txtspl:
			if( i != ','):
				sql += unichr(int(i))
		#sql = str(consulta.format('hex')) #decode(0x0F)
		print(sql)
		lista = []
		tmp = []
		conn = lite.connect("/home/peli/SqliteDbs/SqliteData.s3db")
		if(conn is  None): 
			print("No se abrio base de datos")
		curs=conn.cursor()
		curs.execute(str(sql).encode('UTF-8'))
		for row in curs.fetchall():
			#print(row)
			tmp.append(str(row).encode('utf-8'))
			
		for ix in tmp:
			lista.append(str(ix).encode('utf-8'))
			#print(ix)
		tmp = []
			
		for j in lista:
			tmp.append(str(j).encode('UTF-8'))
		conn.close()
		return tmp
	
		
	@soap(String,_returns = Integer)
	def ExecCommand(self , consulta):
		print(consulta)
		conn = lite.connect("/home/peli/SqliteDbs/SqliteData.s3db")
		try:
			if(conn is  None): 
				print("No se abrio base de datos")
			curs=conn.cursor()
			curs.execute(consulta.encode('utf-8'))
			conn.commit()
			conn.close()
		except sqlite3.Error as er:
			print(er.message)
			conn.rollback
			return 1
		return 0
		
	@soap(String,_returns = Integer)
	def ExecCommandHex(self , elem):
		conn = lite.connect("/home/peli/SqliteDbs/SqliteData.s3db")
		txtspl = elem.split(',')
		del txtspl[len(txtspl) - 1]
		sql = ''
		for i in txtspl:
			if( i != ','):
				sql += unichr(int(i))
		print(sql)
		try:
			if(conn is  None): 
				print("No se abrio base de datos")
			curs=conn.cursor()
			curs.execute(sql.encode('utf-8'))
			conn.commit()
			conn.close()
		except sqlite3.Error as er:
			print(er.message)
			conn.rollback
			return 1
		return 0
    
class localizator(DefinitionBase):
	@soap(String , _returns = Array(Float))
	def GetLocalizacion(self, direccion):
		results = Geocoder.geocode(direccion)
		return results[0].coordinates
		
	@soap(String ,_returns = Boolean)
	def GetValidate(self,direccion):
		return Geocoder.geocode(direccion).valid_address

	@soap(String , _returns = Integer)
	def GetCodePostal(self,direccion):
		results = Geocoder.geocode(direccion)
		return results[0].postal_code

	@soap(Float,Float,_returns= String)
	def GetDireccion(self ,longitud,latitud):
		results = Geocoder.reverse_geocode(longitud,latitud)
		lista = str(results[0])       #.split(','))
		return lista  #formated_address

class gpio(DefinitionBase):
	
	@soap(String)
	def mode(self , mode):
		if(mode == 'BOARD'):
			GPIO.setmode(GPIO.BOARD)
		if(mode == 'BCM'):
			GPIO.setmode(GPIO.BCM)
	@soap(Integer , String)
	def setup_pin(self , pin , modo):
		if(modo == 'IN'):
			GPIO.setup(pin, GPIO.IN)
		if(modo == 'OUT'):
			GPIO.setup(pin, GPIO.OUT)
	
	@soap(Integer , Integer)
	def pin_out(self , pin , status):
		if(status == 1):
			GPIO.output(pin, GPIO.HIGH)
		if(status == 0):
			GPIO.output(pin, GPIO.LOW)
			
	@soap(Integer, _returns = Integer)
	def read_pin(self , pin):
		return int(GPIO.input(pin))

class arduino(DefinitionBase):
	@soap()
	def ConnSerial(self):
		global s 
		s = serial.Serial('/dev/ttyACM0', 19200 , timeout = 4.0)
		try:
			s.open()
			print('PUERTO ABIERTO')
	
		except Exception, e:
			print ("error abriendo puerto: ") + str(e)
			
	@soap(_returns = String )
	def Recibir_dato(self):
		valor = s.readline()
		return valor
		
	@soap(String , _returns = Boolean)
	def Enviar_Dato(self , dato):
		s.write(dato)
		return True
		
	@soap(Integer ,_returns = Integer)
	def dametoma(self,valor):
		return valor *2



if __name__=='__main__':
    try:
        from wsgiref.simple_server import make_server
        soap_application = soaplib.core.Application([Funciones,Database,localizator,gpio,arduino],'xml')
        wsgi_application = wsgi.Application(soap_application)
        
        server = make_server(servidor, puerto, wsgi_application)
        server.serve_forever()
        
    except ImportError:
        print "Error: Requiere Python >= 2.7"

    
    


