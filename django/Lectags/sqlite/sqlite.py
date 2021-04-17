import sys
import sqlite3
import requests
from sqlite.jsonMod import Json

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
            
    def compEnvioNoVacio(self):
        rows = None
        cuantos = 0
        try:
            self.c = self.conn.cursor()
            self.c.execute( 'SELECT COUNT(*) FROM indice' )
            rows = self.c.fetchall()
            cuantos = rows[0][0]
        except Exception as e:
            print('Error determinando cuantos(COUNT(*) '+ str(e))
		
        return cuantos

    def leerDato( self ):
        txt = ''
        self.c = self.conn.cursor()
        rows = None
        link = None
        try:
            self.c.execute( 'SELECT indice FROM indice' )
            rows = self.c.fetchall()
            self.c.execute('SELECT link FROM link')
            link = self.c.fetchone()[0]
            
        except Exception as e:
            print('Error en la lectura de datos. '+ str(e))
        
        js = None
        Jeis = Json()
        mtz = []
        for dat in rows:
            js = dat[0].split('*')
            mtz.append(js)

        #print('Matrix: ', mtz)

        txt = Jeis.crearJson(mtz)

        try:
            resp = requests.get(link + txt )
            if resp.ok == True:
                self.c.execute( 'DELETE FROM indice' )
                self.conn.commit()
            print('Respuesta: ', resp.ok)
        except  Exception as e:
            print('Error: ', str(e))

        
    def revPedido( self ):
        txt = ''
        self.c = self.conn.cursor()
        rows = None
        link = None
        try:
            self.c.execute( 'SELECT indice FROM indice' )
            rows = self.c.fetchall()
            self.c.execute('SELECT link FROM link')
            link = self.c.fetchone()[0]
            
        except Exception as e:
            print('Error en la lectura de datos. '+ str(e))
        
        for dat in rows:
            print('Fila: ' +dat[0]+'\n')
            txt += '|' + str(dat[0])
        
        txt = txt[ 1 : ] + '|' + 'ReViSiOn'
        print( 'Dato: ', txt )

        try:
            resp = requests.get( link + txt )# envia datos
            print('\nRespuesta: ', resp.ok)
        except Exception as e:
            print('\nError en la lectura de datos. '+ str(e))
        
    def borrarPedido(self):
        try:
            self.c = self.conn.cursor()
            self.c.execute( 'DELETE FROM indice' )
            self.conn.commit()
        except Exception as e:
            print('Error: ', str(e))
        

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
            




            




    


        
        


