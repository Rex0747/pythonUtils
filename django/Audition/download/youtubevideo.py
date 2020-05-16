import pafy
#import pickle
import os
import sys
#import pyglet
from pydub import AudioSegment
import pydub.utils
from Audition.settings import BASE_DIR
from glob import glob
import os
import subprocess
errores = " "


def DescargarListaVideos( enlace , ruta ):
    playlist = pafy.get_playlist(enlace)
    directorio = playlist['title']
    print("El directorio creado es" + directorio )
    #creamos directorio con el nombre de la lista.
    if not os.path.exists( ruta + '/' + directorio):
        print("Creando directorio " + ruta + '/' + directorio)
        try:
            os.mkdir(ruta + '/' + directorio)
        except:
            print("No se ha podido crear ese directorio,tiene caracteres no validos.\n")
            print("Primero tienes que volver a meter la ruta , en el siguiente tienes que meter el directorio.\n")
            ruta = input("Mete la ruta a mano.\n")
            directorio = input("Mete el directorio a mano\n")
            os.mkdir(ruta + '/' + directorio)
    print("Ruta a descargar los ficheros: " + ruta + '/' + directorio + '\n')
    print("Autor " + playlist['author'])
    nvideos = len(playlist['items'])
    print("Numero de videos a descargar " + str(nvideos) + '\n')
    for i in range(0, nvideos):
        datos = ""
        print(playlist['items'][i]['pafy'])
        v = playlist['items'][i]['pafy'].getbest(preftype="mp4")
        name = v.title
        print(v.resolution + "  " + v.extension + '\n')
        try:
            datos = v.download(filepath=ruta + '/' + directorio +'/' + name + "." + v.extension)
        except Exception as excepcion:
            print("Excepcion de tipo " + str(excepcion))
            #errores =+ excepcion.message
        print('Video creado correctamente' + datos)
        print(name)

def DescargarVideo( enlace ):
    ruta = os.path.join( BASE_DIR ,'download/temp' )
    video = pafy.new( enlace )
    # print(video.title)
    # print(video.duration)
    # print(video.rating)
    # print(video.author)
    # print(video.length) 
    # print(video.thumb)
    # print(video.videoid)
    # print(video.viewcount)
    name = video.title.replace(' ','')
    # print(name)
    # print("Autor " + video.author)
    # print("Duracion " + video.duration)
    data = video.getbest(preftype="mp4")
    try:
        data.download(filepath=ruta + '/' + name + "." + data.extension)
        print('Video creado correctamente ' )
    except Exception as excepcion:
        print("Excepcion de tipo " + str(excepcion))
    
    return name.replace(' ','') + "." + data.extension

def DescargarAudio( url ):
    ruta = os.path.join( BASE_DIR ,'download/temp' )
    video = pafy.new(url)
    # print(video.title)
    # print(video.duration)
    # print(video.rating)
    # print(video.author)
    # print(video.length)
    # print(video.thumb)
    # print(video.videoid)
    # print(video.viewcount)
    name = ''
    patron = r"!3$%&/(=?¿¡{}- ,;<º\ª>*+)"
    for i in video.title:
        if i not in patron:
            name += i
    print('VIDEO-TITLE: ' + video.title)
    print('VIDEO.NAME: ' + name)
    #name = video.title.replace(" ", "")
    audio = video.getbestaudio(preftype="any") #any
    fila = ruta + "/" + name + "." + audio.extension
    f = audio.download( fila)
    #print('Bajado: '+str(f)) 
    fichero = convertir2(fila)
    return fichero

def convertir2(fichero):
    fexport = fichero + ".mp3"

    f = open(fexport,'wb')
    f.close()

    print("Convirtiendo fichero " + fexport + " a mp3\n")
    print("Exportando a mp3 ")
    try:
        print("Segmentando.")
        exec = sys.prefix + '/ffmpeg.exe -i ' + fichero + ' -vn -ab 128k -ar 44100 -y ' + fexport
        print(exec)
        res=subprocess.run( exec, shell=True)
        #res=subprocess.run(r'G:/ffmpeg/ffmpeg.exe -i ' + i + ' -vn -ab 128k -ar 44100 -y ' + i +'.mp3', shell=True)
        print(res.check_returncode())

    except Exception as ValueError:
        print("Errores al convertir " + str(ValueError))
    print("Conversion finalizada.")
    return fexport


def convertir(fichero):
    fexport = fichero + "_1.mp3"
    f = open(fexport , "+wb")
    f.close()
    print("Convirtiendo fichero " + fexport + " a mp3\n")
    print("Exportando a mp3 ")
    try:
        print("Segmentando.")
        home = sys.prefix # escribe el home de python, los programas de compresion estan en el home de python
        AudioSegment.ffmpeg = home + '/ffmpeg.exe'   #r'C:/Programas/Portable_APP\WPy64-3810/python-3.8.1.amd64\Scripts/ffmpeg.exe'
        AudioSegment.converter = home + '/ffmpeg.exe'   #r'C:/Programas/Portable_APP\WPy64-3810/python-3.8.1.amd64\Scripts/ffmpeg.exe'
        sonido = AudioSegment.from_file(fichero)
        print("Exportando.")
        sonido.export( fexport , format="mp3" , bitrate="128k" )
    except Exception as ValueError:
        print("Errores al convertir " + str(ValueError))
    print("Conversion finalizada.")
    return fexport
            
    