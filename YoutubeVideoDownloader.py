#!/usr/bin/python
# -*- coding: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import pafy
#import pickle
import os
import pyglet
from pydub import AudioSegment
import pydub.utils
from glob import glob
import gc

errores = " "
mode = 0

def getvid(url , modo , ruta):
    if modo == '1':
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
            fila = []
            print(playlist['items'][i]['pafy'])
            v = playlist['items'][i]['pafy'].getbest(preftype="mp4")
            name = v.title
            print(v.resolution + "  " + v.extension + '\n')
            try:
                datos = v.download(filepath=ruta + '/' + directorio +'/' + name + "." + v.extension)
            except Exception as excepcion:
                print("Excepcion de tipo " + excepcion.message)
                #errores =+ excepcion.message
            print('Video creado correctamente' + datos)
            print(name)
            
    elif modo == '0':
        print(str(enlace)+ "   "+ str(mode) + "     "+ str(ruta))
        video = pafy.new(url)
        print(video.title)
        print(video.duration)
        print(video.rating)
        print(video.author)
        print(video.length)
        #print(video.keywords)
        print(video.thumb)
        print(video.videoid)
        print(video.viewcount)
        name = video.title
        print(name)
        print("Autor " + video.author)
        print("Duracion " + video.duration)
        data = video.getbest(preftype="mp4")
        try:
            datos =  data.download(filepath=ruta + '/' + name + "." + data.extension)
            print('Video creado correctamente ' )
        except Exception as excepcion:
            print("Excepcion de tipo " + excepcion.message)
    elif modo == '2':
        #Descargar solo audio
        video = pafy.new(url)
        print(video.title)
        print(video.duration)
        print(video.rating)
        print(video.author)
        print(video.length)
        print(video.thumb)
        print(video.videoid)
        print(video.viewcount)
        name = video.title.replace(" ", "")
        audio = video.getbestaudio(preftype="any") #any
        fila = ruta + "/" + name + "." + audio.extension
        f = audio.download( fila)
        print('Bajado: '+str(f)) 
        convertir(fila)
        

def convertir(fichero):
    fexport = fichero + "_1.mp3"
    f = open(fexport , "+wb")
    f.close()
    print("Convirtiendo fichero " + fexport + " a mp3\n")
    print("Exportando a mp3 ")
    import logging
    import psutil
    print('MEMORIA: ' + str( psutil.virtual_memory()))
    try:
        print("Segmentando.")
        AudioSegment.ffmpeg = r'C:\Programas\Portable_APP\Python_3.8_Portable\python-3.8.3rc1.amd64\ffmpeg.exe'
        AudioSegment.converter = r'C:\Programas\Portable_APP\Python_3.8_Portable\python-3.8.3rc1.amd64\ffmpeg.exe'
        sonido = AudioSegment.from_file(fichero)
        print("Exportando.")
        sonido.export( fexport , format="mp3" , bitrate="128k" )
    except Exception as ValueError:
        print("Errores al convertir " + str(ValueError))
    print("Conversion finalizada de " + fexport)


if __name__ == "__main__":
    ruta = 'C:/temp'#'/home/peli/Videos'
    enlace = ""  # Aqui va enlace de la lista
    print("DownloadsYoutube V1.0 todos los derechos reservados.\n")
    mode = input("Teclea 0 si vas a bajar un fichero , 1 si es una lista , 2 solo audio, 3 convertir a mp3.\n")
    enlace = input("Pega ahora el enlace\n")
    print("La ruta por defecto de descarga es " + ruta + '\n')
    ralt = input("Para modificar la ruta pulsa 0 ,Para dejarlo asi pulsa enter \n")
    if ralt == '0':
        ruta = input("Introduce ruta a descargar\n")

    if mode == '3':
        ruta = input('Escribe ruta donde se encuentran los .webm')
        ruta = ruta.replace("\\" , "" )
        files = glob(ruta + '/*.webm')
        for i in files:
            print('Convirtiendo ' + str(i))
            convertir(i)
            
        
    else:
        getvid(enlace , mode , ruta)
        
        
        
        
    #music = pyglet.resource.media("C:\Lune.mp3")
    #music.play()
    #pyglet.app.run()
    #print(errores)

