# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:25:44 2020

@author: Pedro
"""

from glob import glob
import os
import subprocess

print('Convertidor de webm a mp3 por libreria ffmpeg\n')
ruta = input('Teclea dir donde estan los webm\n')
#ffmpeg -i "${FILE}" -vn -ab 128k -ar 44100 -y "${FILE%.webm}.mp3"
files = glob(ruta + '*.webm')
for i in files:
    print('Comprimiendo ' + i )
    res=subprocess.run(r'G:/ffmpeg/ffmpeg.exe -i ' + i + ' -vn -ab 128k -ar 44100 -y ' + i +'.mp3', shell=True)
    #print(subprocess.call( 'G:/ffmpeg/ffmpeg.exe','-i',i,'-vn','-ab 128k','-ar 44100','-y','res.mp3' ))
    #print(subprocess.call( ['G:/ffmpeg/ffmpeg.exe',],shell=True ))
    #res.check_returncode()