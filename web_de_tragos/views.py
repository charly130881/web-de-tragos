from django.shortcuts import render, redirect
from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.urls import reverse
from .forms import ContactoForm, RecetaForm, RecetaFormValidado, TamañoForm, CaracteristicaForm, FuncionForm
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

#RECETAS

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


#TAMAÑO

def tamaño_index(request):
    tamaños = Tamaño.objects.all()
    return render(request, 'web_de_tragos/administracion/tamaños/index.html', {'tamaños': tamaños})


class TamañosListView(ListView):
    model = Tamaño
    context_object_name = 'tamaños'
    template_name = 'web_de_tragos/administracion/tamaños/index.html'


class TamañosView(View):
    form_class = TamañoForm
    template_name = 'web_de_tragos/administracion/tamaños/nuevo.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tamaños_index')

        return render(request, self.template_name, {'formulario': form})


def tamaños_editar(request, id_tamaño):
    try:
        tamaño = Tamaño.objects.get(id=id_tamaño)
    except Tamaño.DoesNotExist:
        return render(request, 'web_de_tragos/administracion/404_admin.html')
    
    if request.method == "POST":
        formulario = TamañoForm(request.POST, instance=tamaño)
        if formulario.is_valid():
            formulario.save()
            return redirect('tamaños_index')
    else:
        formulario = TamañoForm(instance=tamaño)

    return render(request, 'web_de_tragos/administracion/tamaños/editar.html', {'formulario': formulario, 'id_tamaño': id_tamaño})


def tamaños_eliminar(request, id_tamaño):
    try:
        tamaño = Tamaño.objects.get(id=id_tamaño)
    except Tamaño.DoesNotExist:
        return render(request, 'web_de_tragos/administracion/404_admin.html')
    
    tamaño.delete()
    return redirect('tamaños_index')


#CARACTERISTICA

def caracteristica_index(request):
    caracteristicas = Caracteristica.objects.all()
    return render(request, 'web_de_tragos/administracion/caracteristicas/index.html', {'caracteristicas': caracteristicas})


class CaracteristicasListView(ListView):
    model = Caracteristica
    context_object_name = 'caracteristicas'
    template_name = 'web_de_tragos/administracion/caracteristicas/index.html'


class CaracteristicasView(View):
    form_class = CaracteristicaForm
    template_name = 'web_de_tragos/administracion/caracteristicas/nuevo.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('caracteristicas_index')

        return render(request, self.template_name, {'formulario': form})


def caracteristicas_editar(request, id_caracteristica):
    try:
        caracteristica = Caracteristica.objects.get(id=id_caracteristica)
    except Caracteristica.DoesNotExist:
        return render(request, 'web_de_tragos/administracion/404_admin.html')
    
    if request.method == "POST":
        formulario = CaracteristicaForm(request.POST, instance=caracteristica)
        if formulario.is_valid():
            formulario.save()
            return redirect('caracteristicas_index')
    else:
        formulario = CaracteristicaForm(instance=caracteristica)

    return render(request, 'web_de_tragos/administracion/caracteristicas/editar.html', {'formulario': formulario, 'id_caracteristica': id_caracteristica})


def caracteristicas_eliminar(request, id_caracteristica):
    try:
        caracteristica = Caracteristica.objects.get(id=id_caracteristica)
    except Caracteristica.DoesNotExist:
        return render(request, 'web_de_tragos/administracion/404_admin.html')
    
    caracteristica.delete()
    return redirect('caracteristicas_index')

#FUNCION

def funcion_index(request):
    funciones = Funcion.objects.all()
    return render(request, 'web_de_tragos/administracion/funciones/index.html', {'funciones': funciones})


class FuncionesListView(ListView):
    model = Funcion
    context_object_name = 'funciones'
    template_name = 'web_de_tragos/administracion/funciones/index.html'


class FuncionesView(View):
    form_class = FuncionForm
    template_name = 'web_de_tragos/administracion/funciones/nuevo.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('funciones_index')

        return render(request, self.template_name, {'formulario': form})


def funciones_editar(request, id_funcion):
    try:
        funcion = Funcion.objects.get(id=id_funcion)
    except Funcion.DoesNotExist:
        return render(request, 'web_de_tragos/administracion/404_admin.html')
    
    if request.method == "POST":
        formulario = FuncionForm(request.POST, instance=funcion)
        if formulario.is_valid():
            formulario.save()
            return redirect('funciones_index')
    else:
        formulario = FuncionForm(instance=funcion)

    return render(request, 'web_de_tragos/administracion/funciones/editar.html', {'formulario': formulario, 'id_funcion': id_funcion})


def funciones_eliminar(request, id_funcion):
    try:
        funcion = Funcion.objects.get(id=id_funcion)
    except Funcion.DoesNotExist:
        return render(request, 'web_de_tragos/administracion/404_admin.html')
    
    funcion.delete()
    return redirect('funciones_index')


