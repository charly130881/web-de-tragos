from django.shortcuts import render
from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.template import loader

from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.

def index(request):   
    return render(request,'web_de_tragos/publica/index.html', {'titulo': 'Inicio'})

def about(request):
    template = loader.get_template('web_de_tragos/publica/about.html')
    context = {'titulo': 'About'}
    return HttpResponse(template.render(context, request))    

def tragos(request):
    template = loader.get_template('web_de_tragos/publica/tragos.html')
    context = {'titulo': 'Tragos'}
    return HttpResponse(template.render(context, request))   

def contacto(request):
    template = loader.get_template('web_de_tragos/publica/contacto.html')
    context = {'titulo': 'Contacto'}
    return HttpResponse(template.render(context, request)) 