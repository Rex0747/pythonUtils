from django.shortcuts import render
from django.http import HttpResponse
from .youtubevideo import DescargarVideo, DescargarAudio, DescargarListaVideos
from Audition.settings import BASE_DIR
import os
import glob


def DescargarVideoYoutube( request ):
    url = ''
    ruta = os.path.join( BASE_DIR ,'download/temp/','*' )
    frem = glob.glob( ruta ) #'C:/Users/Pedro/OneDrive/Documentos/Python/django/Audition/download/temp/*')
    try:
        for f in frem:
            print('Borrando fichero: ' + f )
            os.remove( f )
    except Exception as e:
        print('Excepcion: ' + str( e ))

    if request.method ==  'POST' and request.POST['url']:
        url = request.POST['url']
        nombre = DescargarVideo( url )

        fila = os.path.join( BASE_DIR ,'download/temp', nombre )
        print( 'Fichero a descargar: ' + fila )
        with open( fila , 'rb') as fh:
            #print('ENTRO')
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename( fila )
            return response

    
    return render( request , 'dvideo.html',{'url': url })

def DescargarAudioYoutube( request ):
    url = ''
    ruta = os.path.join( BASE_DIR ,'download/temp/','*' )
    frem = glob.glob( ruta ) 
    try:
        for f in frem:
            print('Borrando fichero: ' + f )
            os.remove( f )
    except Exception as e:
        print('Excepcion: ' + str( e ))

    if request.method ==  'POST' and request.POST['url']:
        url = request.POST['url']
        nombre = DescargarAudio( url )
        

        #fila = os.path.join( BASE_DIR ,'download/temp', nombre )
        fila = nombre 
        print( 'Fichero a descargar: ' + fila )
        with open( fila , 'rb') as fh:
            #print('ENTRO')
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename( fila )
            return response

    
    return render( request , 'daudio.html',{'url': url })

