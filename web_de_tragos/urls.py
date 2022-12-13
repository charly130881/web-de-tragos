from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name='inicio'),
    path('about/',views.about,name='about'),
    path('tragos/',views.tragos,name='tragos'),
    path('contacto/',views.contacto,name='contacto'),
    path('administracion', views.index_administracion, name='inicio_administracion'),
    
    # Administracion
    path('administracion/recetass/editar/<int:id_receta>', views.recetas_editar, name='recetas_editar'),
    path('administracion/recetas/eliminar/<int:id_receta>', views.recetas_eliminar, name='recetas_eliminar'),
    # path('administracion/recetas/nuevo/', views.recetas_nuevo, name='recetas_nuevo'),
    # path('administracion/recetas', views.recetas_index, name='recetas_index'),
    path('administracion/recetas/nuevo/', views.RecetasView.as_view(), name='recetas_nuevo'),
    path('administracion/recetas', views.RecetasListView.as_view(), name='recetas_index'),
    
]