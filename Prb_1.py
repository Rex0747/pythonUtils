import sys
import cv2
import numpy
import matplotlib
import re
import string
import binascii
import datetime
import random
import sqlite3
import json
import numpy as np
from matplotlib import pyplot as plt
#import qrcode , qrcode1
import pyqrcode

dic = { 'A' :'Burzum', 'B': 'Kreator', 'C':'Sodom', 'D': 'Helloween' }
#dic2 ='AC-DC','JUDAS PRIEST','IRON MAIDEN','SEPULTURA','DARKTRONE'

a , b = 'MOTORHEAD', 'RAMMSTEIM'
#a = dic
print( str(a) )
print( str(b) )

print(json.dumps(a))

# print(cv2.__version__)
# cv2.namedWindow('image', cv2.WINDOW_FULLSCREEN)
# foto = cv2.imread('C:/temp/CC.jpg', 1)
# print('foto: ' + str(foto))

#cv2.imshow('image', foto)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
# plt.imshow( foto, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
# plt.show()

# cap = cv2.VideoCapture(0)
# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # Display the resulting frame
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()

# cap = cv2.VideoCapture('C:/Users/Pedro/Downloads/Therion-Live2007.mp4')
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
#     cv2.imshow('frame', gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

# Create a black image
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
#img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
#img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
ubicacion = '12-4-1'
code = '001243'
#nombre = 'ESPUMA DETERGENTE Y DESINFECTANTE PARA LIMPIEZA DE MOBILIARIO INSTRUNET SURFA´SAFE 2925 (E/750 ML.)'
#pacto = '12'
#gfh = 'HN4B'
#lista = (ubicacion, code, pacto, gfh )
#delim = '|'
#articulo = delim.join(lista)
#print(articulo)

articulo = input('Lee lector qr')
tmp = pyqrcode.QRCode( articulo, error='H', version=3, mode=None, encoding='iso-8859-1')
#tmp = pyqrcode.create(articulo)
#print(tmp.text())
enviar = input('Enviar linea S/N ' + articulo)
if(enviar == 'S' or enviar == 's'):
    print('Codigo enviado')
    tmp.show()
    lista =articulo.split('|')
    print(str(lista))
    print('Guardar en BBDD')
else:
    print('Linea cancelada.')
    
#-----------------------------------------------------
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
#c = canvas.Canvas("C:/tmp/hola_mundo.pdf")
#c.drawString(10,750,"Hola mundo pdf!")
#c.save()    


canvas = canvas.Canvas("C:/tmp/hola_mundo.pdf", pagesize=letter)
w, h = letter
print('W: ',w, ' H: ',h)
print('Tipo: ', type(letter))
canvas.setLineWidth(.3)
canvas.setFont('Helvetica', 12)

canvas.drawImage('C:/Users/Pedro/OneDrive/Imágenes/96A.jpg',5,25, width=550, height=550)
canvas.drawImage('C:/Users/Pedro/OneDrive/Imágenes/96A.jpg',15,25, width=550, height=550)
canvas.drawImage('C:/Users/Pedro/OneDrive/Imágenes/96A.jpg',25,25, width=550, height=550)

canvas.drawString(30,750,'CARTA DE PRUEBA')
canvas.drawString(30,735,'RICARDOGEEK.COM')
canvas.drawString(500,750,"27/10/2016")
canvas.line(480,747,580,747)
 
canvas.drawString(275,725,'ESTIMADO:')
canvas.drawString(500,725,"<NOMBRE>")
canvas.line(378,723,580,723)
 
canvas.drawString(30,703,'ETIQUETA:')
canvas.line(120,700,580,700)
canvas.drawString(120,703,"<ASUNTO DE LA CARTA GENERICO>")
canvas.showPage()


# canvas.grid(xlist, ylist)
# canvas.bezier(x1, y1, x2, y2, x3, y3, x4, y4)
# canvas.arc(x1,y1,x2,y2)
# canvas.rect(x, y, width, height, stroke=1, fill=0)
# canvas.ellipse(x1,y1, x2,y2, stroke=1, fill=0)
# canvas.wedge(x1,y1, x2,y2, startAng, extent, stroke=1, fill=0)
# canvas.circle(x_cen, y_cen, r, stroke=1, fill=0)
# canvas.roundRect(x, y, width, height, radius, stroke=1, fill=0) 

canvas.save()









    