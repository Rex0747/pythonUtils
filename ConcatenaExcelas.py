import pandas as pd

#import openpyxl

exc1 = pd.read_excel('c:/temp/BSAN.xlsx')
exc2 = pd.read_excel('c:/temp/DIAL.xlsx')
#print( exc1 )

ex1 = [['pk_modulo','pk_estanteria','pk_ubicacion','pk_division','codigo','nombre','pacto','minimo','cod_doblecajon']]
ex2 = [['pk_modulo','pk_estanteria','pk_ubicacion','pk_division','codigo','nombre','pacto','minimo','cod_doblecajon']]

dt = [ex1,ex2]
file = pd.concat(dt)
file.to_excel('c:/temp/concatenados.xlsx')