# Generated by Django 4.2.2 on 2023-06-21 19:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_biblioteca', '0017_remove_prestamo_libro_reserva_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo_libro',
            name='reserva',
            field=models.BooleanField(default=False, verbose_name='Confirme su reserva'),
        ),
        migrations.AlterField(
            model_name='prestamo_libro',
            name='fecha_prestamo_fin',
            field=models.DateField(default=datetime.datetime(2023, 7, 21, 16, 23, 56, 411782), verbose_name='Fin del prestamo'),
        ),
    ]