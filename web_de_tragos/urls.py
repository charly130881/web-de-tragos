<<<<<<< HEAD
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
    # ---------------recetas
    path('administracion/recetas/editar/<int:id_receta>', views.recetas_editar, name='recetas_editar'),
    path('administracion/recetas/eliminar/<int:id_receta>', views.recetas_eliminar, name='recetas_eliminar'),
    path('administracion/recetas/nuevo/', views.RecetasView.as_view(), name='recetas_nuevo'),
    path('administracion/recetas', views.RecetasListView.as_view(), name='recetas_index'),
    
    # ---------------tamaño
    path('administracion/tamaños/editar/<int:id_tamaño>', views.tamaños_editar, name='tamaños_editar'),
    path('administracion/tamaños/eliminar/<int:id_tamaño>', views.tamaños_eliminar, name='tamaños_eliminar'),
    path('administracion/tamaños/nuevo/', views.TamañosView.as_view(), name='tamaños_nuevo'),
    path('administracion/tamaños', views.TamañosListView.as_view(), name='tamaños_index'),
    
    # ---------------funcion
    path('administracion/funciones/editar/<int:id_funcion>', views.funciones_editar, name='funciones_editar'),
    path('administracion/funciones/eliminar/<int:id_funcion>', views.funciones_eliminar, name='funciones_eliminar'),
    path('administracion/funciones/nuevo/', views.FuncionesView.as_view(), name='funciones_nuevo'),
    path('administracion/funciones', views.FuncionesListView.as_view(), name='funciones_index'),
    
    # ---------------caracteristica
    path('administracion/caracteristicas/editar/<int:id_caracteristica>', views.caracteristicas_editar, name='caracteristicas_editar'),
    path('administracion/caracteristicas/eliminar/<int:id_caracteristica>', views.caracteristicas_eliminar, name='caracteristicas_eliminar'),
    path('administracion/caracteristicas/nuevo/', views.CaracteristicasView.as_view(), name='caracteristicas_nuevo'),
    path('administracion/caracteristicas', views.CaracteristicasListView.as_view(), name='caracteristicas_index'),
    
]
=======
>>>>>>> 760f479ce591e835c09039ac06154c43b31b771b
