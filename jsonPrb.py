# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 23:25:27 2020

@author: Pedro
"""

class Json:
     
    jeiso = "["

    bloque = """{"gfh":"","nombre":"","""
            
            
    def __init__(self):
        pass

    def crearJson(self,data):
        # j = 0
        # for i in range(len(data)):
        #     if j < len(data) -1:
        #         self.jeiso += self.bloque + "},"
        #         j += 1
        #     else:
        #         self.jeiso += self.bloque + "}"
                        
        # self.jeiso += "]"
        # print('jeiso: ', self.jeiso)
        # #js = self.jeiso.replace("\'", "\"")
        
        v = json.loads( """{"gfh":"H8NA","nombre":"IZ020"}""" )
        
        print('V: ', str(v))
        j = 0
        print('filas: ', len(v))
        print(data)
        for i in v:
            print('Vuelta: ', str(j))
            i['gfh'] = data[j][0]
            i['nombre'] = data[j][1]
            j += 1
        return json.dumps(v)
            
    #print(jeiso)
    #print(type(jeiso))
    
import json

lista = [["H8NA", "IZL020"]] #, ['H8NA', 'IZ020'], ['H8NB', 'IZL025'], ['H8NB', 'IZ026'], ['H8NC', 'IZ010'], ['H7NA', 'IZ034'], ['H7NA', 'IZL024'], ['H7NB', 'IZ036']]

f_json = Json()

txtJson = f_json.crearJson(lista)
print( 'JSON: ', txtJson)    