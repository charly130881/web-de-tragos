from django.db import models

# Create your models here.

# class estudiante(models.Model):
#     nombre = models.CharField(max_length=100, verbose_name='name del estudiante')
#     apellido =models.CharField(max_length=150, verbose_name='apellido del estudiante')
#     email = models.EmailField(max_length=150, verbose_name='email del estudiante')
#     dni = models.IntegerField(verbose_name='DNI del estudiante')
    
# class Tipo(models.Model):
#     tipo = models.CharField(max_length=25, verbose_name='Tipo')

class Tamaño(models.Model):
    tamaño = models.CharField(max_length=25, verbose_name='Tamaño', default=1)
    info_tamaño = models.TextField(("info del tamaño"))

class Funcion(models.Model):
    funcion = models.CharField(max_length=25, verbose_name='Funcion', default=1)
    info_Funcion = models.TextField(("info de funcion"))
  
class Caracteristica(models.Model):
    caracteristica = models.CharField(max_length=25, verbose_name='Caracteristica', default=1)
    info_caracteristica = models.TextField(("info de caracteristica"))
    
# class Usuario(models.Model):
#     usuario = models.CharField(max_length=25, verbose_name='nombre de usuario')

class Receta(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='nombre')
    # usuario = models.ForeignKey(Usuario, verbose_name="user", on_delete=models.CASCADE)
    fecha_creacion = models.DateField (verbose_name='Fecha de creación')
    # imagen = models.ImageField(upload_to='Imagenes/', verbose_name='Imagen', null=True)
    Ingredientes = models.TextField(verbose_name='Ingredientes') 
    preparacion = models.TextField(verbose_name='Preparacion')
    # tipo = models.ManyToManyField(Tipo)
    tamaño = models.ForeignKey(Tamaño, verbose_name="tamaño", on_delete=models.CASCADE)
    funcion = models.ForeignKey(Funcion, verbose_name="Función", on_delete=models.CASCADE)
    caracteristica = models.ForeignKey(Caracteristica, verbose_name="Caracteristica", on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if self.nombre.upper() == 'AGUA':
            raise ValueError("El Agua no es un trago, es... solo agua")
        else:
            super().save(*args, **kwargs)