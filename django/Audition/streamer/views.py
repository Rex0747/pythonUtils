from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.shortcuts import render

# Create your views here.

@xframe_options_sameorigin
def streamer( request ):

    link = 'https://youtu.be/YODCM26JXOY'

    return render( request, 'ini.html', { 'link': link,} )
