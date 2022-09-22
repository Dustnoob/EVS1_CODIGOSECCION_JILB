from multiprocessing import reduction
from re import S
from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def display(request):
    return HttpResponse(
        '<h1>Hola Esta es mi APP1</h1>'
    )

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = '<b>Fecha y hora: </b>' + str(dt)
    return HttpResponse(s)

def display2(request):
    return HttpResponse(
        '<ul><li>1uno</li><ul>'
        '<ul><li>2dos</li></ul>'
        '<ul><li>3tres</li></ul>'
        '<ul><li>4cuatro</li></ul>'
        '<ul><li>5cinco</li></ul>'
        '<ul><li>6seis</li></ul>'
        '<ul><li>7siete</li></ul>'
        '<ul><li>8ocho</li></ul>'
        '<ul><li>9nueve</li></ul>'
        '<ul><li>10diez</li></ul>'
    )