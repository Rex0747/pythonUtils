#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
import os
import qr
from gpiozero import LED
from time import sleep
import time
import datetime
import platform
import keyboard
from sqlite.sqlite import baseData

led_green = LED(17)
led_red = LED(23)

#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
# 
#GPIO.setup(22, OUT)
#GPIO.setup(27, OUT)

def opposite(device):
    for value in device.values:
        yield not value

def change(device, tiempo):    #Cambiar estado de pin
    if device.is_active:
        device.off()
    else:
        device.on()
    device.source = opposite(device)
    #print('Led Encendido: ', device.active_high, ' Activo: ', device.is_active)
    sleep(tiempo)

def ledOn(device):
    device.on()

def ledOff(device):
    device.off()

def ledOnTime(device, tiempo):
    device.on()
    print('Led encendido.')
    sleep(tiempo)
    device.off()
    print('Led apagado.')

def ledRafaga(device,npulsos,tiempo):
    for i in range(npulsos):
        change(device,0)
        print('Estado: ',device.is_active)
        sleep(tiempo)

    
def inicio(data):
    #print(data)
    if data == enviar:
        enviarPedido()
    elif data == comprobar:
        revisarPedido()
    elif data == borrar:
        borrarPedido()
    else:
        db = baseData(ruta_db )
        res = db.compararTags(data)
        if res == False:
            print('Insertando: ', str(data))
            db.insertarDato( data )
            #poner aqui chivato de luz verde de ok
            change(led_green)
        else:
            print('Error... Referencia duplicada, no se incluye en pedido.')   # Poner aqui chivato luz roja de error.
            print('DATO: ', data)
            ledOnTime(led_red, 3)

def enviarPedido():
    db = baseData(ruta_db )
    cuantos = db.compEnvioNoVacio()
    print('Nfilas: ', str(cuantos))
    if cuantos > 0:
        db.leerDato()
    else:
        print('No se puede enviar un pedido vacio')
    
def revisarPedido():
    db = baseData( ruta_db )
    db.revPedido()
    
def borrarPedido():
    db = baseData(ruta_db )
    db.borrarPedido()

def comprobarFormato():
    mtx = data.split(delim)
    if (len(mtx) == 6 or data == borrar or data == enviar or data == comprobar ):
        return True
    else:
        return False

#_______Declaraciones____________



# led.on()
# led.source = opposite(led)
# print('Led Encendido: ', led.active_high, ' Activo: ', led.is_active)
# sleep(2)
# led.off()
# led.source = opposite(led)
# print('Led Encendido: ', led.active_high, ' Activo: ', led.is_active)
# sleep(2)

time.sleep(1)

sistema = platform.system()

txt = ''
lista = []
delim = '*'
borrar = '1551'
comprobar = '021992'
enviar = '010304'

ledRafaga(led_green,9,0.2)
sleep(2)
ledOnTime(led_red, 4)

#______End Declaraciones__________

if(__name__ == '__main__'):
    txt = ''
    v = ''
    ruta = os.getcwd()
    ruta_db = ruta + '/db.s3db'
    print('OS: ', sistema)
    print('Directotio actual: ', ruta)
    #while v != '028187':
    while(True):
        events = keyboard.record('enter')
        txt = keyboard.get_typed_strings(events)
        # play these events
        #keyboard.play(events)
        v = list(txt)[0]
        data = v.replace('+','*')
        fila = open( ruta + '/lg.log','a+')
        fila.write('Linea: ' + data +'\n')
        fila.close()
        inicio(data)





