# Generated by Django 4.2.1 on 2023-05-31 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_biblioteca', '0006_alter_libro_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='descripcion',
            field=models.TextField(max_length=3000, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='idioma',
            field=models.CharField(max_length=20, verbose_name='Idioma'),
        ),
    ]