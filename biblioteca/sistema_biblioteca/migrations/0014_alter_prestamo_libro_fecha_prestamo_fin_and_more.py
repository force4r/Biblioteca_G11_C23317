# Generated by Django 4.2.1 on 2023-06-13 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_biblioteca', '0013_delete_bibliotecario_remove_libro_reserva_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo_libro',
            name='fecha_prestamo_fin',
            field=models.DateField(null=True, verbose_name='Fin del prestamo'),
        ),
        migrations.AlterField(
            model_name='prestamo_libro',
            name='fecha_prestamo_inicio',
            field=models.DateField(auto_now_add=True, verbose_name='Inicio del prestamo'),
        ),
    ]