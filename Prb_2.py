import sys
import sqlite3

def func(a , b):
	return (a+b,a*b,str(a)+str(b))
lista = [123,"hola",'A',12.2,"pepe"]
lista.append("new")
print(lista)
txt = "Vamos muy bien.. borrachos como cubas y que...?"
print(txt[0:])
dic = {"1":10,"2":20}
dic["3"] =  30
dic["4"] = 40
print(dic["4"])


dic["2"] = 6
dic["3"] = 8
print(dic["2"])
print(dic["3"])

for i in dic:
	print(i,":",dic[i])# iterar diccionario

for k, v in dic.items():
   print( k, ":", v)

for t in dic.items():
	print(t) 

def f(x, y):
	x = x + 3
	y.append(23)
	print(x, y)
x = 22
y = [22]
f(x, y)
print (x, y)
print("___________________________________________\n")
print(func(12,34))
print(sqlite3.version)
conn = sqlite3.connect('C:\\Users\\peli\\Documents\\SqliteDbs\\data.s3db')
conn.execute('select * from usuarios')
c = conn.cursor()
for i in c:
	c.fetchone()
conn.close()
