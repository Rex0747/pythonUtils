import pyqrcode
import png

rutafichero = 'c:/tmp/code.png'
print('Teclea texto plano a qenerar en codigo QR.')
datos = raw_input('Teclea texto plano a qenerar en codigo QR.')
url = pyqrcode.create(datos.decode('cp1252') ,encoding='utf-8' )# error='L', version=27, mode='binary')  #('http://uca.edu')
url.svg('uca-url.svg', scale=8)
url.eps('uca-url.eps', scale=2)
url.png( rutafichero , scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
print('Codigo QR creado en '+ rutafichero )
#print(url.terminal(quiet_zone=1))