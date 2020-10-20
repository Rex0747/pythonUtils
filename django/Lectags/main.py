import sys
import qr
#from prb1 import evento
from pynput import keyboard as kb
from pynput.keyboard import _win32
from sqlite.sqlite import baseData

txt = ''
lista = []


def inicio():
    #print(data)
    if data == '010304':
        enviarPedido()
    elif data == '021992':
        revisarPedido()
    elif data == '1551':
        borrarPedido()
    else:
        db = baseData('db.s3db' )
        res = db.compararTags(data)
        if res == False:
            print('Insertando: ', str(data))
            db.insertarDato( data )
            #poner aqui chivato de luz verde de ok
        else:
            print('Error...Duplicado')   # Poner aqui chivato luz roja de error.

def enviarPedido():
    db = baseData('db.s3db' )
    db.leerDato()
    
def revisarPedido():
    db = baseData('db.s3db' )
    db.revPedido()
    
def borrarPedido():
    db = baseData('db.s3db' )
    db.borrarPedido()
    
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
        #print(str(type(txt)))
        lista.clear()
        inicio()
    else:
        #print('Tecla: ', tecla.char)
        #print('Typo: ',type(tecla))
        if type(tecla)==_win32.KeyCode:
            if tecla.char in ['0','1','2','3','4','5','6','7','8','9']:
                lista.append(tecla.char)

if(__name__ == '__main__'):

    with kb.Listener(pulsa) as escuchador:
        escuchador.join()
