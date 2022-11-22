from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
from datetime import datetime


# Create your views here.
# def index(request):
#     template= loader.get_template('index.html')
#     return HttpResponse(template.render(request))

def index(request):
    return render(request, 'web_de_tragos/index.html')


def about(request):
    return render(request, 'web_de_tragos/about.html')


def tragos(request):
    return render(request, 'web_de_tragos/tragos.html')


def contact(request):
    return render(request, 'web_de_tragos/contact.html')
