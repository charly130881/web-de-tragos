# Generated by Django 3.2.14 on 2022-12-16 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_de_tragos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='imagen',
            field=models.ImageField(null=True, upload_to='Imagenes/', verbose_name='Imagen'),
        ),
    ]
