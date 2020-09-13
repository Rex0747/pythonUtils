import sys
import qr
#from prb1 import evento
from pynput import keyboard as kb
from sqlite.sqlite import baseData


txt = ''
#data = ''
lista = []

def inicio():
    print(data)
    db = baseData('db.s3db' )
    db.insertarDato( data )

def pulsa(tecla):
    global data
    data = ''
    #print('Se ha pulsado la tecla ' + str(tecla))
    if tecla == kb.Key.esc:
        exit()

    if tecla == kb.Key.enter:
        txt = "".join(map( str, lista))
        for i in txt:
            if i != chr(39):
                data += str(i)
        #print(data)
        #print('Valor: '+  txt)
        #print(str(type(txt)))
        lista.clear()
        inicio()
    else:
        lista.append(tecla)

if(__name__ == '__main__'):

    with kb.Listener(pulsa) as escuchador:
        escuchador.join()





#Qrcode = qr.qr()
#print( 'Imprime: ' + str(Qrcode.getVal()))
