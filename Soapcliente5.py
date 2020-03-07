# -*- coding: utf-8 -*-

from suds.client import Client
#from geopy.geocoders import Nominatim , GoogleV3 , Bing
#from geopy import *
#from geopy.geocoders import *
#from geopy.distance import lonlat, distance
import  json
import unicodedata



def ConvDicci( res ):
    dicci = { }
    for i in range(len(res[0])):
        val = res[0][i].split(':')
        dicci.update( { val[0] : val[1] })
    return dicci

def ConvTupla( res):
    lista = [ ]
    for i in range( len(res[0]) ):
        lista.append( res[0][i].split(',') )
    return lista

def Getordinal( sql ):
    lista = ""
    l = len(sql)

    for i in sql:
        lista += str(ord(i)) + ','
    return lista

def ConvLista( lista ):
    ret = [ ]
    for i in lista:
        for j in i[1]:
            j = j.replace('[', '')
            j = j.replace(']', '')
            j = j.replace("'", '')
            l = j.split(',')
            ret.append( l )
        return ret


url_service = 'http://192.168.1.34:7789/?wsdl'       #'http://www.webservicex.net/globalweather.asmx?WSDL'

client = Client(url_service)

#client.options.cache.clear()

list_of_methods = [method for method in client.wsdl.services[0].ports[0].methods]

print( list_of_methods )

#client.service.SelectGeocoder( 1 )



#geolocator = Nominatim(user_agent="LocalizatorV1.0")



#location = geolocator.geocode("calle amposta 2 Madrid SP")
#location2 = geolocator.geocode("calle alfonso martinez conde 3 Madrid SP")
#print(location.address)
#print((location.latitude, location.longitude))
#print(location2.address)
#print((location2.latitude, location2.longitude))
#
#siteB = (location2.latitude, location2.longitude)
#siteA = (location.latitude, location.longitude)
#
#siteALat = location.latitude
#siteAlon = location.longitude
#siteBLat = location2.latitude
#siteBlon = location2.longitude
#print("SiteALat: " ,  siteALat )
#print("SiteB: " ,  siteB[0] ,  siteB[1])
# #print(distance(lonlat(*siteA), lonlat(*siteB)).kilometers)
#


#dir =  client.service.GetLocalDireccion("calle Helena de Troya Madrid SP")
#print( dir )
#
#km =  client.service.GetLocalDir( '40.4045627' , '-3.5990658' , '40.381915' , '-3.76634' , 5 )  #40.381915, -3.766341
#print( "Desde A a B hay: " + str(km) )
#
#cp = client.service.GetZipcode("50 calle monteleon Madrid SP")
#print( cp )

#rev = client.service.GetNombre( "40.424057, -3.617121" )
#print( rev )


# geolocator = Nominatim ( user_agent = "specify_your_app_name_here" )
#
# location = geolocator.geocode("19 calle Opticos Madrid SP") #geolocator.reverse( "52.509669, 13.376294" )
# print ( location.address )
#
# print (( location.latitude , location.longitude ))
#
# print ( location.address )  #.raw['address']['postcode'] )
#
# print ( json.dumps( location.raw ) )
#
# dir , punto  = geolocator.reverse( "52.509669, 13.376294")
#
# print( "------------" )
#
# print( dir )
# print ( punto )


# from pprint import pprint
# import requests
# r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID={APIKEY}')
# pprint(r.json())


#import openweather
#from datetime import datetime

# create client

# ow = openweather.OpenWeather('&APPID=4769135f104eac2443a750e99f8656')  #&APPID=4769135f104eac2443a750e99f8656
#
# # find weather stations near me
# stations = ow.find_stations_near(
#     7.0,  # longitude
#     50.0, # latitude
#     100   # kilometer radius
# )
#
# # iterate results
# for station in stations:
#     print( station )
#
# # get current weather at Cologne/Bonn airport
# # (station id = 4885)
# print(ow.get_weather(4885))
#
# # historic weather
# start_date = datetime(2018, 10, 23)
# end_date = datetime(2018, 10, 26)
#
# # default: hourly interval
# print (ow.get_historic_weather(4885, start_date, end_date))

# # daily aggregates
# print(ow.get_historic_weather(4885, start_date, end_date, "day"))

# import pyowm
#
# owm = pyowm.OWM('4769135f104eac2443a750e99f865635')
# observation = owm.weather_at_place("Madrid , Spain")
# w = observation.get_weather()
# tomorrow = pyowm.timeutils.tomorrow()
# wind = w.get_wind()
# print(w)
# print(wind)
# temperature = w.get_temperature('celsius')
# print(temperature)
# print(tomorrow)
#__________________________________________________

#res = client.service.GetWind( "Madrid , Spain" )
#res = ConvDicci(res)
#print( type(res))
#print(res['Velocidad Viento'])
#print(res['Orientacion Viento'])
#print( res[0][0][0] )
#print( res[0][1][0] )
#
#res = client.service.GetTemp("Madrid , Spain" )
#res = ConvDicci(res)
#print(res['Temperatura Maxima'])
#print(res['Temperatura Minima'])
#print(res['Temperatura Actual'])
#print( res['15.0'] )
#print( res['Temperatura maxima. '] )
#print( res['Temperatura actual. '] )


#__________________________________________________________________-
# import pygeoip
# from pygeoip import *
# #try:
# host = '89.10.161.192'
# rawdata = pygeoip.GeoIP('/home/peli/Documentos/GeoLiteCity.dat')
# data = rawdata.record_by_addr(host) #record_by_addr(host)
# country = data['country_name']
# city = data['city']
# longi = data['longitude']
# lat = data['latitude']
# time_zone = data['time_zone']
# area_code = data['area_code']
# country_code = data['country_code']
# region_code = data['region_code']
# dma_code = data['dma_code']
# metro_code = data['metro_code']
# country_code3 = data['country_code3']
# zip_code = data['postal_code']
# continent = data['continent']
#
# print '[*] IP Adress: ',host
# print '[*] City: ',city
# print '[*] Region Code: ',region_code
# print '[*] Area Code: ',area_code
# print '[*] Time Zone: ',time_zone
# print '[*] Dma Code: ',dma_code
# print '[*] Metro Code: ',metro_code
# print '[*] Latitude: ',lat
# print '[*] Longitude: ',longi
# print '[*] Zip Code: ',zip_code
# print '[*] Country Name: ',country
# print '[*] Country Code: ',country_code
# print '[*] Country Code3: ',country_code3
# print '[*] Countinent: ',continent
#
# #except:
#     #print("[*] Please verify your ip !")

#res = client.service.GetdataIp('89.10.161.191')

#res = ConvDicci( res )
#print( type(res))
#print(res['Ciudad'])

res = client.service.RetornarConsultaHex( Getordinal("SELECT * FROM usuarios WHERE id > 0") )
v = ConvLista( res )
for i in v:
    for j in i:
        #j = j.encode('iso8859-1')
        j = j.encode("ascii",errors='replace')
        print( j )
        print(type( j ))
    print( '____________')

print( v )
#file = open('/home/peli/borrame.txt','w')
#res = ConvTupla(res)
# for i in res:
#     #print( i )
#     for j in i:
#         k = j.replace("u'" , '')
#         j = k.replace("'" , '')
#         o = unicodedata.normalize('NFKC' , j )
#         file.write( o )
#         print( o )

#print( res )
#file.close()

#res = client.service.ExecCommandHex( Getordinal("drop table pasajero"))
#print(res)

