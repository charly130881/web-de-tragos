from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import UserCreateView
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path('',views.index,name='inicio'),
    path('about/',views.about,name='about'),
    path('tragos/',views.tragos,name='tragos'),
    path('contacto/',views.contacto,name='contacto'),
    path('receta/<int:nro_id>',views.receta, name='receta'),

     # Login   
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', LoginView.as_view(template_name='web_de_tragos/publica/login.html'), name='login'),   
    path('accounts/register', UserCreateView.as_view(template_name='web_de_tragos/publica/register.html'), name='registro'), 
    path('accounts/logout/', LogoutView.as_view(template_name='web_de_tragos/publica/logout.html'), name='logout'),
]
