import sqlite3


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
        print('Vamos a Insertar....', dato )
        print('Tipo: ', type( dato ))
        try:
            #self.conn.execute('INSERT INTO indice( indice )VALUES( ? )', dato )
            self.c = self.conn.cursor()
            self.c.execute( 'INSERT INTO indice VALUES( ? )', ( dato, ) )
            self.conn.commit()

        except Exception as e:
            self.conn.rollback()
            print('Error al insertar dato.')
            print( str(e) )

        finally:
            self.conn.close()

        
        


