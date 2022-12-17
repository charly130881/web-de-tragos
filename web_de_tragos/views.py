from django.shortcuts import render, redirect
from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.urls import reverse
from .forms import ContactoForm, RecetaFormValidado, TamañoForm, CaracteristicaForm, FuncionForm
from .forms import ContactoForm, RecetaForm, RecetaFormValidado
from django.contrib import messages
from datetime import datetime
from .models import Receta, Tamaño, Caracteristica, Funcion
from django.views import View
from django.views.generic import ListView

# Create your views here.

def index(request):   
    return render(request,'web_de_tragos/publica/index.html', {'titulo': 'Inicio'})

def about(request):
    template = loader.get_template('web_de_tragos/publica/about.html')
    context = {'titulo': 'About'}
    return HttpResponse(template.render(context, request))    

def tragos(request):
    recetas = Receta.objects.all().order_by('fecha_creacion')
    return render(request, 'web_de_tragos/publica/tragos.html',{'tragos':recetas})

def receta(request, nro_id):
    receta = Receta.objects.get(id=nro_id)
    return render(request, 'web_de_tragos/publica/receta.html', {'receta':receta, 'nro_id':nro_id})

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


