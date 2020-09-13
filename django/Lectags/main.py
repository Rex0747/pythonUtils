#import sys
#import qr
#from prb1 import evento
from pynput import keyboard as kb

txt = ''
#data = ''
lista = []

def inicio():
    print(data)
    

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

with kb.Listener(pulsa) as escuchador:
    escuchador.join()


<<<<<<< HEAD
Qrcode = qr.qr()
print( 'Imprime: ' + str(Qrcode.getVal()))

=======
>>>>>>> 73f78497a074c29243251c14a3f07e5702bf86db
