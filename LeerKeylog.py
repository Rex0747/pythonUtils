import sys

fila=open('c:/tmp/keylog.txt','r')
txt = ''
for i in fila:
    
    txt += i[:-1]

print(txt)