# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 20:51:41 2020

@author: Pedro
"""
from comExcel.excel import Excell
from comExcel.xlsx import comprobarExcel

file = 'H4NB_IZ014.xlsx'
x = Excell( file )
fichero = x.leer_fichero()


c = comprobarExcel(fichero)

dup = c.comprobarDuplicados()
if dup != None:
    for i in dup:
        print('Duplicados: ', i )
        
vac = c.comprobarVacios()
if vac != None:
    for i in vac:
        print('Vacios: ', i )
        
dgfh = c.comprobarGfhDisp()
if dgfh != None:
    for i in dgfh:
        print('GfhsDisp: ', i )


