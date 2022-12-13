from django.shortcuts import render, redirect
from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.urls import reverse
from .forms import ContactoForm
from django.contrib import messages

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
    if request.method == "POST":
        # Creao la instancia populada con los datos cargados en pantalla
        contacto_form = ContactoForm(request.POST)
        # Valido y proceso los datos.
        if contacto_form.is_valid():
            messages.success(request, "Formulario cargado con éxito")
    else:
        # Creo el formulario vacío con los valores por defecto
        contacto_form = ContactoForm()
    return render(request, "web_de_tragos/publica/contacto.html", {'contacto_form': contacto_form})

""" def contacto2(request):
    template = loader.get_template('web_de_tragos/publica/contacto.html')
    context = {'titulo': 'Contacto'}
    return HttpResponse(template.render(context, request)) 
 """