# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 22:24:01 2020

@author: Pedro
"""

from gtts import gTTS
from pygame import mixer
from playsound import playsound
from os import  remove


texto = "gfh y dispositivo creado correctamente."
idioma = 'es'

audio = gTTS(text = texto,  lang = idioma, slow = False )
audio.save('C:/temp/prueba.mp3')


sound = r"C:/temp/prueba.mp3"
playsound(sound)
#remove("C:/temp/prueba.mp3")



# mixer.init()    
# mixer.music.load('C:/Users/Pedro/OneDrive/Documentos/Python/prueba.mp3')
# mixer.music.play()

# while mixer.music.get_busy() == True:
#     continue
# mixer.music.stop()
# mixer.music.unpause()
# mixer.quit()
