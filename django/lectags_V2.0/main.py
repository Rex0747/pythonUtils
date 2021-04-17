#! /home/pi/Python/lectags/env/bin/python3.7
# -*- coding: utf-8 -*-
import qr
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
# 
#GPIO.setup(22, OUT)
#GPIO.setup(27, OUT)
import time
import datetime
import platform
import keyboard
from sqlite.sqlite import baseData

time.sleep(1)

sistema = platform.system()




txt = ''
lista = []
delim = '*'
borrar = '1551'
comprobar = '021992'
enviar = '010304'


def inicio(data):
    #print(data)
    if data == enviar:
        enviarPedido()
    elif data == comprobar:
        revisarPedido()
    elif data == borrar:
        borrarPedido()
    else:
        db = baseData('/home/pi/Python/lectags/db.s3db' )
        res = db.compararTags(data)
        if res == False:
            print('Insertando: ', str(data))
            db.insertarDato( data )
            #poner aqui chivato de luz verde de ok
        else:
            print('Error... Referencia duplicada, no se incluye en pedido.')   # Poner aqui chivato luz roja de error.
            print('DATO: ', data)
def enviarPedido():
    db = baseData('/home/pi/Python/lectags/db.s3db' )
    cuantos = db.compEnvioNoVacio()
    print('Nfilas: ', str(cuantos))
    if cuantos > 0:
        db.leerDato()
    else:
        print('No se puede enviar un pedido vacio')
    
def revisarPedido():
    db = baseData('/home/pi/Python/lectags/db.s3db' )
    db.revPedido()
    
def borrarPedido():
    db = baseData('/home/pi/Python/lectags/db.s3db' )
    db.borrarPedido()

def comprobarFormato():
    mtx = data.split(delim)
    if (len(mtx) == 6 or data == borrar or data == enviar or data == comprobar ):
        return True
    else:
        return False


if(__name__ == '__main__'):
    txt = ''
    v = ''
    print('OS: ', sistema)
    #while v != '028187':
    while(True):
        events = keyboard.record('enter')
        txt = keyboard.get_typed_strings(events)
        # play these events
        #keyboard.play(events)
        v = list(txt)[0]
        data = v.replace('+','*')
        
        fila = open('/home/pi/Python/lectags/lg.log','a+')
        fila.write('Linea: ' + data +'\n')
        fila.close()
        
        inicio(data)
        #mtx.append(v)

