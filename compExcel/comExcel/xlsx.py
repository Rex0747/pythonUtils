# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 20:47:42 2020

@author: Pedro
"""
from comExcel.excel import Excell

class comprobarExcel:
    
    ListaUb = []
    ListaCo = []
    Lista = []
    ubicacion = ''
    codigo = ''

    def __init__(self, lista ):
        #print(lista)
        self.ListaUb.clear()
        self.Lista = lista
        for i in lista:
            ubicacion = str(i[0])+'-'+str(i[1])+'-'+str(i[2])+'-'+str(i[3])
            codigo = str(i[4]) + ' ' + str(i[6])  # codigo + DC
            self.ListaUb.append( ubicacion )
            self.ListaCo.append( codigo )
            ubicacion = None
            codigo = None
        

    def comprobarDuplicados( self ):
        duplic = []
        ind = 0
        ind2 = 1
        #print('ListaUB: ' + str( len(self.ListaUb)))
        for i in self.ListaUb:
            ind2 = ind + 1
            for j in range(  len( self.ListaUb ) - ind2 ):
                if ind2 >= len( self.ListaUb ):
                    ind2 -= 1
                if self.ListaUb[ ind2 ] == i:
                    duplic.append( i )
                ind2 +=1
            ind += 1
        #if len(duplic) > 0:
        return duplic


    def comprobarVacios(self):  #x numero columna y posicion en fila
        x = 2; y = 0
        vacios = []
        for i in self.Lista:
            for j in i:#enumerate(i):
                y += 1
                if j == None or j == '':
                    #print('Vacio: ' + str(i)) 
                    vacios.append( ( Excell.getNombreColumna(y) , x) )
                    
            y = 0
            x += 1
                
        return vacios

    def comprobarGfhDisp(self):
        l = []
        err = []
        ind = 0
        try:
            for i in self.Lista:
                l.append( ( i[9], i[10], i[11] ) )
        except Exception as e:
            print('Exception en ' + str(e))
            return err
        for i in l:
            #print( 'Lista: ' + str( self.Lista[ind][9] ))
            #print( 'Tupla: ' + str( i[0] ))
            if i[0] != self.Lista[0][9]:
                err.append( ( ind + 2 , i[0] ) )
                #print( 'Indice: ' + str( i[0] + '  ' + str( self.Lista[9] ) ) )

            if i[1] != self.Lista[0][10]:
                err.append( ( ind + 2 , i[1] ) )
                #print( 'Indice: ' + str( i[1] + '  ' + str( self.Lista[ind][10] ) ) )

            if i[2] != self.Lista[0][11]:
                err.append( ( ind + 2 , i[2] ) )
                #print( 'Indice: ' + str( i[2] + '  ' + str( self.Lista[ind][12] ) ) )
            
            ind += 1
        if len(err) > 0:
            return err


        