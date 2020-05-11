import requests
import csv

lista = {}
count=0
with open('smart.csv', newline='') as csvread:
	csvfile=csv.reader(csvread,delimiter=',')
	
	for row in csvfile:
		#print(str(row[0]) +'works in the'+ str(row[1]) )
		#print(str(row))
		lista[str(row[0])] = str(row[0])
		count += 1
	print('Procesados '+ str(count) +' enlaces.')

print(str(lista))
print('______________________________________________________________________________')

print(count)
for i in lista:
	code = i
	mtx=i.split(',')
	imagen = requests.get(mtx[1]).content
	with open('c:/temp/DesFotos/Smartphones/' + mtx[0] + '.jpg', 'wb') as handler:
		handler.write(imagen)
print('Proceso finalizado.')
