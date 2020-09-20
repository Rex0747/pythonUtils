import sys
import sqlite3
import requests

class baseData:

    #conn = None

    def __init__(self, db ):
        print( sqlite3.version )
        try:
            self.conn = sqlite3.connect( db )
            print('Conexion a base de datos correcta.')
        except Exception as e:
            self.conn.rollback()
            print('Error al abrir base de datos.')
            print( str(e) )

    def insertarDato(self, dato ):
        #print('Vamos a Insertar....', dato )
        #print('Tipo: ', type( dato ))
        try:
            self.c = self.conn.cursor()
            self.c.execute( 'INSERT INTO indice VALUES( ? )', ( dato, ) )
            self.conn.commit()

        except Exception as e:
            self.conn.rollback()
            print('Error al insertar dato.')
            print( str(e) )

        finally:
            self.conn.close()

    def leerDato( self ):
        txt = ''
        self.c = self.conn.cursor()
        rows = None
        try:
            self.c.execute( 'SELECT indice FROM indice' )
            rows = self.c.fetchall()
            
        except Exception as e:
            print('Error en la lectura de datos. '+ str(e))
        
        for dat in rows:
            txt += '|' + str(dat[0])
        
        txt = txt[1 : ]
        print( 'Dato: ', txt )

        resp = requests.get('http://localhost:8082/etiquetas/'+ txt )
        if resp.ok == True:
            self.c.execute( 'DELETE FROM indice' )
            self.conn.commit()
        print('Respuesta: ', resp.ok)

    def compararTags(self, codigo ):
            self.c = self.conn.cursor()
            try:
                self.c.execute( 'SELECT indice FROM indice WHERE indice=?',(codigo,) )
                rows = self.c.fetchall()
                if len(rows) > 0:
                    return True
                else:
                    return False
            except Exception as e:
                return e
            




            




    


        
        


