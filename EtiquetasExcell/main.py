import  sys
import os
import time
from excell import Excell

xlsx = None
lista = []   #aqui esta la lista donde se agregan todas lineas.
B = ""
R = ""
SB = ""
SR = ""
ultima_fila_blanca = 2;
ultima_fila_roja = 2;
ultima_fila_amarilla = 2;

#def concatenar( inicio , fin ):  #concatena los campos de modulos
    #res = xlsx.leer_rango( inicio , fin )
    #conc = str(res[0])+'-'+str(res[1])+'-'+str(res[2])
    #print(conc)

def selecc_articulo( inicio , fin ):
    res = xlsx.leer_rango( inicio, fin )

def incrementar( ubc ):
    l = len(ubc)
    it = 0
    for i in ubc[:: -1]:
        if (i != '-'):
            it += 1
        else:
            break
    sum = int(ubc[l - it:]) + 1
    return ubc[: l - it] + str(sum)

def addcar( code ):
    res = ""
    l = len( code )
    if( l < 3 ):
        if( l == 2 ):
            res = '#' + code

        if( l == 1 ):
            res = '##' + code
    else:
        return code
    return res


if __name__ == '__main__':
    xlsx = Excell('Etiquetas_Master.xlsx' , 'Plantilla' )
    xlsx.cambiar_hoja('Plantilla')
    print( "Se van a procesar " + str( xlsx.getnumerofilas()) + " filas.")
    #print(xlsx.getnumerocolumnas())
    print("Creando lista etiquetas , espere....")
    id = 0
    for i in range( 2 , xlsx.getnumerofilas()+ 1 ):
        mtx = xlsx.leer_rango("A"+str(i), "N"+str(i) )
        m = mtx.pop(0)
        e = mtx.pop(0)
        u = mtx.pop(0)
        d = mtx.pop(0)
        ubicaciones = str(m) + "-" + str(e) + "-" + str(u)
        mtx.insert(0, ubicaciones)
        lista.append( mtx )
        #print("Numero campos: " + str(len(mtx)))
        mtx = None

    #for i in lista:      #Solo imprime lista a visualizar
    #     print("Linea " + str(id))
    #     print( i )
    #     id += 1

    print("Nfilas: " + str(len(lista)))
    for i in lista:
        B = i[7]
        R = i[8]
        SB = i[9]
        SR = i[10]
        if B:
            #print("Imprime Blanca")
            xlsx.cambiar_hoja('Blancas')
            mtz = [1 , 2 , 3 , 4 , 5]
            mtz[0] = addcar( i[1] ) #codigo
            mtz[1] = i[2]  # nombre
            mtz[2] = i[3]  # pacto
            mtz[3] = i[0]  # ubicacion
            mtz[4] = i[6]  # gfh
            xlsx.insertar_rangofila( mtz , ultima_fila_blanca , 1 )
            ultima_fila_blanca += 1

        if R:    #Hay que poner solucion a incrementar la ubicacion
            #print("Imprime Roja")
            xlsx.cambiar_hoja('Rojas')
            mtz = [1, 2, 3, 4, 5]
            mtz[0] = addcar( i[1] )  # codigo
            mtz[1] = i[2]  # nombre
            mtz[2] = i[3]  # pacto
            mtz[3] = incrementar( i[0] ) # ubicacion
            mtz[4] = i[6]  # gfh
            xlsx.insertar_rangofila(mtz, ultima_fila_roja, 1)
            ultima_fila_roja += 1

        if SB:
            #print("Imprime Soporte Blanca")
            xlsx.cambiar_hoja('Amarillas')
            mtz = [1, 2, 3, 4, 5]
            mtz[0] = addcar( i[1] )  # codigo
            mtz[1] = i[2]  # nombre
            mtz[2] = i[3]  # pacto
            mtz[3] = i[0]  # ubicacion
            mtz[4] = i[6]  # gfh
            xlsx.insertar_rangofila(mtz, ultima_fila_amarilla, 1)
            ultima_fila_amarilla += 1


        if SR:   #Hay que poner solucion a incrementar la ubicacion
            #print("Imprime Soporte Roja")
            xlsx.cambiar_hoja('Amarillas')
            mtz = [1, 2, 3, 4, 5]
            mtz[0] = addcar( i[1] )  # codigo
            mtz[1] = i[2]  # nombre
            mtz[2] = i[3]  # pacto
            mtz[3] = incrementar( i[0] )  # ubicacion
            mtz[4] = i[6]  # gfh
            xlsx.insertar_rangofila(mtz, ultima_fila_amarilla, 1)
            ultima_fila_amarilla += 1

    xlsx.salvarexcell()

    print("------------------------------------")
    print("Se crearon " + str( ultima_fila_blanca - 2 ) + " etiquetas blancas.")
    print("Se crearon " + str( ultima_fila_roja - 2 ) + " etiquetas rojas.")
    print("Se crearon " + str( ultima_fila_amarilla - 2 ) + " etiquetas amarillas.")
    print("Finalizo proceso.")
    #print(lista)