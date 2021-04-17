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
time.sleep(1)

fila = open("/home/pi/Python/lectags/log.log","a")
fila.write('Inicio de lectura a: ' + str(datetime.datetime.now())+'\n')
fila.close()

from pynput import keyboard as kb
from sqlite.sqlite import baseData
import platform

sistema = platform.system()

plataforma = None
if(sistema == 'Windows'):
    from pynput.keyboard import _win32
    plataforma = _win32
if(sistema == 'Linux'):
    from pynput.keyboard import _xorg
    plataforma = _xorg

txt = ''
lista = []
delim = '*'
borrar = '1551'
comprobar = '021992'
enviar = '010304'


def inicio():
    #print(data)
    if data == enviar:
        enviarPedido()
    elif data == comprobar:
        revisarPedido()
    elif data == borrar:
        borrarPedido()
    else:
        db = baseData('db.s3db' )
        res = db.compararTags(data)
        if res == False:
            print('Insertando: ', str(data))
            db.insertarDato( data )
            #poner aqui chivato de luz verde de ok
        else:
            print('Error... Referencia duplicada, no se incluye en pedido.')   # Poner aqui chivato luz roja de error.

def enviarPedido():
    db = baseData('db.s3db' )
    cuantos = db.compEnvioNoVacio()
    print('Nfilas: ', str(cuantos))
    if cuantos > 0:
        db.leerDato()
    else:
        print('No se puede enviar un pedido vacio')
    
def revisarPedido():
    db = baseData('db.s3db' )
    db.revPedido()
    
def borrarPedido():
    db = baseData('db.s3db' )
    db.borrarPedido()

def comprobarFormato():
    mtx = data.split(delim)
    if (len(mtx) == 6 or data == borrar or data == enviar or data == comprobar ):
        return True
    else:
        return False


def pulsa(tecla):
    global data 
    data = ''
    #print('Se ha pulsado la tecla ' + str(tecla))
    if tecla == kb.Key.esc:
        exit()

    if tecla == kb.Key.enter:
        txt = "".join(map( str, lista))
        for i in txt:
            #if i != chr(39):
            data += str(i)

        #print(data)
        #print('Valor: '+  txt)
        
        res = comprobarFormato()
        if res == True:
            lista.clear()
            inicio()
            data = ''
        else:
            print('\nCodigo RFID no compatible.')
            lista.clear()
            data = ''

    else:
        #print('Tecla: ', tecla.char)
        #print('Typo: ',type(tecla))
        lchars = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z',',','.','-','~','*']
        if type(tecla) == _xorg.KeyCode:  #_xorg para linux   _win32 para windows
            if tecla.char in lchars:
                lista.append(tecla.char)
                #print('Tipo: ', type(tecla.char))
                #print(str(lista))

if(__name__ == '__main__'):

    print('OS: ', sistema)
    #print('Typo1: ', type(_xorg))
    #print('Typo2: ', type(plataforma))

    with kb.Listener(pulsa) as escuchador:
        escuchador.start()

