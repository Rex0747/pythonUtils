#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 11/2/2017

@author: peli
'''
# import socket
import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('utf8')
import os
import base64
from os import listdir
import soaplib
from soaplib.core.service import rpc, DefinitionBase, soap
from soaplib.core.model.primitive import String, Integer
from soaplib.core.server import wsgi
from soaplib.core.model.clazz import Array
from soaplib.core.model.primitive import Float
from soaplib.core.model.primitive import Boolean
from soaplib.core.model.primitive import Any
from soaplib.core.model.clazz import ClassModel
import sqlite3
import sqlite3 as lite
import hashlib
from os.path import isfile, join
from pygeocoder import Geocoder  # No funciona ya este servicio
import geopy
from geopy.geocoders import Nominatim, GoogleV3 , Bing
from geopy.distance import lonlat, distance, geodesic , vincenty , great_circle
from geopy import distance
import serial
import pyowm
from pygeoip import *
import pygeoip
import unicodedata
import json
from flask import jsonify

import RPi.GPIO as GPIO
import RPi
import time



servidor = '192.168.1.34'
puerto = 7789


class lista_(ClassModel):
    __namespace__ = "punk.tunk"
    numero = String  # Integer
    calle = String
    pais = String
    codigo = String


class Funciones(DefinitionBase):
    @soap(String , String , _returns=String)
    def GetHash( self, tx , tipo ):
        hs = hashlib.new( tipo )
        hs.update( tx )
        ret = hs.hexdigest()
        return ret


    @soap(String, Integer, _returns=Array(String))
    def say_hello(self, name, times):
        results = []
        for i in range(0, times):
            results.append('Hello, %s' % name)
            return results

    @soap(Integer, Integer, _returns=Integer)
    def suma(self, a, b):
        return a + b

    @soap(String, _returns=String)
    def ConvMay(self, txt):
        ret = ''
        for i in txt:
            car = ord(i) - 32
            ret += chr(car)
            return ret

    @soap(String, _returns=Array(String))
    def devt(self, txt):
        txt += txt

        return txt

    @soap(String, returns=Array(String))
    def _dir(self, ruta='.'):
        if (ruta == None):
            ruta = '/home/peli/'
            # return (arch for arch in listdir(ruta) if isfile(join(ruta, arch)))
            return os.walk(ruta)

    @soap(String, _returns=String)  # @soap(String,_returns = Array(String))
    def get_datos(self, consulta):
        return 'Funciono ' + consulta

    @soap(String, _returns=String)
    def hextostr(self, txt):
        return txt.format(0x0F)


class Database(DefinitionBase):

    dbase = "/home/peli/DataBases/SqliteData.s3db"

    @soap(String, _returns=Array(String))
    def RetornarConsulta(self, consulta):
        print(consulta)
        lista = []
        tmp = []
        conn = lite.connect( self.dbase )
        if (conn is None):
            print("No se abrio base de datos")
        curs = conn.cursor()
        curs.execute(str(consulta).encode('UTF-8'))
        for row in curs.fetchall():
            # print(row)
            tmp.append(str(row).encode('utf-8'))

        for ix in tmp:
            lista.append(str(ix).encode('utf-8'))
        # print(ix)
        tmp = []

        for j in lista:
            tmp.append(str(j).encode('UTF-8'))
        conn.close()
        return tmp

    @soap(String, _returns =  Array( String ) )
    def RetornarConsultaHex(self, elem):
        txtspl = elem.split(',')
        del txtspl[len(txtspl) - 1]
        sql = ''
        for i in txtspl:
            if (i != ','):
                sql += unichr(int(i))
        # sql = str(consulta.format('hex')) #decode(0x0F)
        print(sql)
        lista = []
        tmp = []
        conn = lite.connect( self.dbase )
        if (conn is None):
            print("No se abrio base de datos")
        curs = conn.cursor()
        curs.execute( sql )
        tmp = curs.fetchall()
        #Aqui tmp es una lista segun type()
        for ch in tmp:
            lst = []
            for itm in ch:
                #print( itm )  #Aqui estan los campos individuales.
                lst.append( str( itm ) )
            lista.append( str( lst ) )
        conn.close()
        return lista

    @soap(String, _returns=Integer)
    def ExecCommand(self, consulta):
        print(consulta)
        conn = lite.connect( self.dbase )
        try:
            if (conn is None):
                print("No se abrio base de datos")
            curs = conn.cursor()
            curs.execute(consulta.encode('utf-8'))
            conn.commit()
            conn.close()
        except sqlite3.Error as er:
            print(er.message)
            conn.rollback
            return -1
        print(curs.rowcount)  # Aqui filas afectadas
        return curs.rowcount

    @soap(String, _returns=Integer )
    def ExecCommandHex(self, elem):
        conn = lite.connect( self.dbase )
        txtspl = elem.split(',')
        del txtspl[len(txtspl) - 1]
        sql = ''
        for i in txtspl:
            if (i != ','):
                sql += unichr(int(i))
                #print(sql)
        try:
            if (conn is None):
                print("No se abrio base de datos")
            curs = conn.cursor()
            curs.execute(sql.encode('utf-8'))
            conn.commit()
            conn.close()
        except sqlite3.Error as er:
            print(er.message)
            conn.rollback
            return -1
        print(curs.rowcount) #Aqui filas afectadas
        return curs.rowcount

        # class localizator(DefinitionBase):
        # @soap(String , _returns = Array(Float))
        # def GetLocalizacion(self, direccion):
        # results = Geocoder.geocode(direccion)
        # return results[0].coordinates

        # @soap(String ,_returns = Boolean)
        # def GetValidate(self,direccion):
        # return Geocoder.geocode(direccion).valid_address

        # @soap(String , _returns = Integer)
        # def GetCodePostal(self,direccion):
        # results = Geocoder.geocode(direccion)
        # return results[0].postal_code

        # @soap(Float,Float,_returns= String)
        # def GetDireccion(self ,longitud,latitud):
        # results = Geocoder.reverse_geocode(longitud,latitud)
        # lista = str(results[0])       #.split(','))
        # return lista  #formated_address


class geolocalizator( DefinitionBase ):

    @soap( Integer , _returns = None )
    def SelectGeocoder(self , geocod ):
        global geolocator
        print("Geolocalizacion con GeoPy.")
        if (geocod == 1):
            geolocator = Nominatim(user_agent="LocalizatorV1.0")
            print("Geocoder seleccionado: NOMINATIM")
        elif (geocod == 2):
            geolocator = GoogleV3()
            print("Geocoder seleccionado: GOOGLE-V3")
        elif ( geocod == 3):
            print("Geocoder seleccionado: BING")
            geolocator = Bing("OIu8w90rr4")

    @soap(Float, Float, Float, Float, Integer,_returns = Float)
    def GetLocalDir(self, siteAlat, siteAlon, siteBlat, siteBlon, mode ):
        global geolocator
        siteA = (siteAlat, siteAlon)
        siteB = (siteBlat, siteBlon)
        if ( mode == 1):
            return distance.distance(lonlat(siteAlat, siteAlon), lonlat(siteBlat, siteBlon)).kilometers
        elif ( mode == 2):
            return distance.distance(siteA, siteB).km
        elif ( mode == 3):
            return geodesic(siteA, siteB).kilometers
        elif ( mode == 4):
            return vincenty(siteA , siteB).kilometers
        elif ( mode == 5):
            return great_circle(siteA , siteB).kilometers
        else:
            print("Seleccion modo no valido")
            return None

    @soap(String, returns=String )
    def GetZipcode(self, direccion ):
        global geolocator
        #self.geolocator = Nominatim(user_agent="LocalizatorV1.0")  #GoogleV3()
        self.location = geolocator.geocode( direccion )
        return self.location.raw

    @soap(String, _returns=Array(Float))
    def GetLocalDireccion(self, direccion):
        global geolocator
        #self.geolocator = Nominatim(user_agent="LocalizatorV1.0")
        self.location = geolocator.geocode(direccion)
        return (self.location.latitude, self.location.longitude)

    @soap( String , _returns = String)
    def GetNombre(self , cord ):
        global geolocator
        #geolocator = GoogleV3()
        try:
            dir , p  = geolocator.reverse( cord )
            return dir
        except Exception as e:
            print( e.message())
            return None

class weather( DefinitionBase ):

    key = 'c4473896f922fc8f308fb978be94cdfc'

    @soap( String , _returns = Array(String) )
    def GetTemp(self , site):

        #key = '4769135f104eac2443a750e99f865635'
        owm = pyowm.OWM( self.key )
        observador = owm.weather_at_place( site )
        w = observador.get_weather()
        #tomorrow = pyowm.timeutils.tomorrow()
        #wind = w.get_wind()
        temp = w.get_temperature('celsius')
        tm = ('Temperatura Maxima:' + str(temp['temp_max']))
        tmi= ('Temperatura Minima:' + str(temp['temp_min']))
        ta = ('Temperatura Actual:' + str(temp['temp']))
        ret = [ ]
        ret.append(tm)
        ret.append(tmi)
        ret.append(ta)
        return ret

    @soap(String, _returns = Array(String))
    def GetWind(self , site  ):

        #key = '4769135f104eac2443a750e99f865635'
        owm = pyowm.OWM( self.key)
        observador = owm.weather_at_place(site)
        w = observador.get_weather()
        wind = w.get_wind()
        ret = []
        ret.append( "Velocidad Viento: " +  str(wind['speed']) )
        ret.append( "Orientacion Viento: " +  str(wind['deg']) )
        return ret


class Geoip(DefinitionBase):

    @soap( String , _returns = Array(String))
    def GetdataIp(self , host ):
        geoip = pygeoip.GeoIP("/home/peli/DataBases/GeoLiteCity.dat")
        data = geoip.record_by_addr(host) #record_by_addr(host)
        #return jsonify( data ) #return jsonify(ip_data)  #No funciona bien
        ret = []
        ret.append( "Pais:" + str(data['country_name'] ))
        ret.append( "Ciudad:" + str(data['city']))
        ret.append( "Longitud:" + str(data['longitude']))
        ret.append( "Latitud:" + str(data['latitude']))
        ret.append( "Zona Horaria:" + str(data['time_zone']))
        ret.append( "Codigo Area:" + str(data['area_code']))
        ret.append( "Codigo Pais:" + str(data['country_code']))
        ret.append( "Codigo Region:" + str(data['region_code']))
        ret.append( "Codigo DMA:" + str(data['dma_code']))
        ret.append( "Codigo Metro:" + str(data['metro_code']))
        ret.append( "Codigo Postal:" + str(data['postal_code']))
        ret.append( "Continente:" + str(data['continent']))
        return ret


class Gpio( DefinitionBase ):

    @soap( String )
    def Mode(self , mode):
        if(mode == 'BOARD'):
            GPIO.setmode(GPIO.BOARD)
        if(mode == 'BCM'):
            GPIO.setmode(GPIO.BCM)


    @soap(Integer , String , Integer)
    def Setup_Pin(self , pin , modo , pullup_down ):
        if(modo == 'IN' and pullup_down == 1 ):
            GPIO.setup( pin, GPIO.IN , pull_up_down=GPIO.PUD_UP )
        if (modo == 'IN' and pullup_down == 0 ):
            GPIO.setup( pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
        if (modo == 'IN' and pullup_down == 2 ):
            GPIO.setup( pin, GPIO.IN )
        if(modo == 'OUT'):
            GPIO.setup( pin, GPIO.OUT  )


    @soap(Integer , Integer)
    def Pin_Out(self , pin , status):
        if(status == 1):
            GPIO.output(pin, GPIO.HIGH)
        if(status == 0):
            GPIO.output(pin, GPIO.LOW)

    @soap(Integer, _returns = Integer)
    def Pin_In(self , pin):
        return int(GPIO.input(pin))

    @soap(  _returns = String )
    def RetVersion(self  ):
        return GPIO.VERSION

    @soap( )
    def CleanUp(self ):
        GPIO.cleanup()

    @soap( Integer , Integer , Integer , _returns = Integer )
    def RGB_init( self , r , g , b):
        try:
            global red , green , blue
            red = GPIO.PWM( 0 , 250 )
            green = GPIO.PWM( 1, 250)
            blue = GPIO.PWM( 2 , 250 )
            red.start( r )
            green.start( g )
            blue.start( b )
            return 0
        except Exception as e:
            print( e.message)
            return -1

    @soap(Integer, Integer, Integer, _returns=Integer)
    def CambiarDuty(self , r , g , b ):
        try:
            global red, green, blue
            red.ChangeDutyCycle( r )
            red.ChangeDutyCycle( g )
            red.ChangeDutyCycle( b )
            return 0
        except Exception as e:
            print(e.message)
            return -1

    @soap(Integer , _returns = Integer)
    def CambiarFrecuencia(self , f ):
        try:
            global red, green, blue
            red.ChangeFrequency( f )
            green.ChangeFrequency( f )
            blue.ChangeFrequency( f )
            return 0
        except Exception as e:
            print( e.message)
            return -1


    @soap( _returns = Integer)
    def Stop_PWM(self):
        try:
            global red, green, blue
            red.stop()
            green.stop()
            blue.stop()
            GPIO.cleanup()
            return 0
        except BaseException as e:
            print( e. message )
            return -1


    @soap( _returns = Integer)
    def Eliminar( self ):
        try:
            global red, green, blue
            red = None
            green = None
            blue = None
            return 0
        except:
            return -1


class Arduino( DefinitionBase ):
    @soap()
    def ConnSerial(self):
        global s
        s = serial.Serial('/dev/ttyACM0', 19200, timeout=4.0)
        try:
            s.open()
            print('PUERTO ABIERTO')

        except Exception as  e:
            print ("error abriendo puerto: ") + str(e)

    @soap(_returns=String)
    def Recibir_dato(self):
        valor = s.readline()
        return valor

    @soap(String, _returns=Boolean)
    def Enviar_Dato(self, dato):
        s.write(dato)
        return True

    @soap(Integer, _returns=Integer)
    def dametoma(self, valor):
        return valor * 2


if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server

        soap_application = soaplib.core.Application([ Funciones, Arduino, Gpio, Database, geolocalizator , weather , Geoip ], 'xml') #xml    tns
        wsgi_application = wsgi.Application(soap_application)

        server = make_server(servidor, puerto, wsgi_application)
        server.serve_forever()

    except ImportError:
        print ("Error: Requiere Python >= 2.7")





