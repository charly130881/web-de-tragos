from django.shortcuts import render, redirect
from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.urls import reverse
from .forms import ContactoForm, RecetaForm, RecetaFormValidado
from django.contrib import messages
from datetime import datetime
from .models import Receta
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
 
def index_administracion(request):
    variable = 'test variable'
    return render(request, 'web_de_tragos/administracion/index_administracion.html', {'variable': variable})


def recetas_index(request):
    recetas = Receta.objects.all().order_by('fecha_creacion')
    return render(request, 'web_de_tragos/administracion/recetas/index.html', {'recetas': recetas})


class RecetasListView(ListView):
    model = Receta
    context_object_name = 'recetas'
    template_name = 'web_de_tragos/administracion/recetas/index.html'
    ordering = ['fecha_creacion']


class RecetasView(View):
    form_class = RecetaFormValidado
    template_name = 'web_de_tragos/administracion/recetas/nuevo.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recetas_index')

        return render(request, self.template_name, {'formulario': form})


def recetas_editar(request, id_receta):
    try:
        receta = Receta.objects.get(id=id_receta)
    except Receta.DoesNotExist:
        return render(request, 'web_de_tragos/administracion/404_admin.html')
    
    if request.method == "POST":
        formulario = RecetaForm(request.POST, instance=receta)
        if formulario.is_valid():
            formulario.save()
            return redirect('recetas_index')
    else:
        formulario = RecetaForm(instance=receta)

    return render(request, 'web_de_tragos/administracion/recetas/editar.html', {'formulario': formulario, 'id_receta': id_receta})


def recetas_eliminar(request, id_receta):
    try:
        receta = Receta.objects.get(id=id_receta)
    except Receta.DoesNotExist:
        return render(request, 'web_de_tragos/administracion/404_admin.html')
    
    receta.delete()
    return redirect('recetas_index')
