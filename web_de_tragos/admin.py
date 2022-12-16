from django.contrib import admin
from web_de_tragos.models import Receta
from web_de_tragos.models import Caracteristica, Funcion, Tamaño

admin.site.register(Receta)
admin.site.register(Caracteristica)
admin.site.register(Funcion)
admin.site.register(Tamaño)
