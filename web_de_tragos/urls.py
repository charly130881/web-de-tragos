from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name='inicio'),
    path('about/',views.about,name='about'),
    path('tragos/',views.tragos,name='tragos'),
    path('contacto/',views.contacto,name='contacto'),
    path('accounts/', include('django.contrib.auth.urls')),
]