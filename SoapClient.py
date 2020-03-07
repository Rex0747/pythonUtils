# -*- coding: UTF-8 -*-
from suds.client import Client
import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF-8')
cl = Client('http://192.168.1.34:7789/?wsdl')
#res = cl.service.say_hello("Hola Periko.", 1)
#for i in res:
#	print (i)
#res = cl.service.suma(sys.argv[1], sys.argv[2])
#print('El resultado es ',res)
#res = cl.service.ConvMay(sys.argv[1])
#print(res) 
#txt = 'po' #sys.argv[1]
#txt = raw_input("Teclea texto a Hashear\n")
#res = cl.service.hashc(str(txt))
#print(res)
cl.options.cache.clear()
#lista = []
#tmp = []
#res = cl.service.ExecCommand('UPDATE usuarios SET id = "ADCCADB5" where id = 4197')
#if(res == 0):
#	print('Salio de lujo')
#else:
#	print('Na una puta mierda')
#print(res)
#for i in res:#
#	for j in i:
#		lista.append(j)
#lista.pop(0)
#if len(lista) >= 2:
#	del lista[0]
#print(lista)
#for k in lista:
#	for l in k:
#		tmp.append(l)
#for s in tmp:
#	print(s)
l = cl.service.GetLocalizacion('Calle Minerva 27 madrid')   #40.4281824  -3.6204905
print(l)
lista = cl.service.GetDireccion(40.40219 , -3.59982)
print(lista)

cl.service.mode('BOARD')
cl.service.setup_pin(11, 'OUT')
cl.service.pin_out(11, 1)
cl.service.pin_out(11, 0)
cl.service.setup_pin(11, 'IN')

#cl.service.ConnSerial()
#for i in range(1500):
#	print(cl.service.Recibir_dato())
#b = cl.service.Enviar_Dato('2334')
consulta = "SELECT * FROM ubicaciones WHERE modulo = 2"
list_num = []
for i in consulta:
	list_num.append(int(ord(i)))

print(type(list_num))
print(len(list_num))

lista_ret = cl.service.RetornarConsultaHex(list_num)
#for i in lista_ret:
#	print(i)
print("Valor retornado " )
print(lista_ret)
print(len(lista_ret))

print("Finalizo programa")
	


