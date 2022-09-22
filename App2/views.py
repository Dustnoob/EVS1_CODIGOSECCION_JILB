from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display1(request):
    return HttpResponse(
        '<h2>Hola Esta es la App2</h2>'
        '<ul><li>lista1</li></ul>'
        '<ul><li>lista2</li></ul>'
        '<ul><li>lista3</li></ul>'
        '<ul><li>lista4</li></ul>'
        '<ul><li>lista5</li></ul>'
        '<ul><li>lista6</li></ul>'
        '<ul><li>lista7</li></ul>'
        '<ul><li>lista8</li></ul>'
        '<ul><li>lista9</li></ul>'
    )

def display2(request):
    return HttpResponse('<h1>Segunda Página con Texto</h1>'
        '<text>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has beens standard dummy text ever since , when an unknown printer took a galley of scrambled it to make a specimen book. It has survived only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised the the release of Letraset sheets containing Lorem Ipsum passages,more recently desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</text>')
