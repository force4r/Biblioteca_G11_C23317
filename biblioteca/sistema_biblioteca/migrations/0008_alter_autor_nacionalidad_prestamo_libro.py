# Generated by Django 4.2.1 on 2023-06-03 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_biblioteca', '0007_alter_libro_descripcion_alter_libro_idioma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='nacionalidad',
            field=models.CharField(max_length=15, verbose_name='Nacionalidad'),
        ),
        migrations.CreateModel(
            name='Prestamo_Libro',
            fields=[
                ('fecha_prestamo_inicio', models.DateField(verbose_name='Inicio del prestamo')),
                ('fecha_prestamo_fin', models.DateField(verbose_name='Fin del prestamo')),
                ('lector', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='sistema_biblioteca.lector', verbose_name='Usuario asociado al préstamo')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_biblioteca.libro', verbose_name='Libro')),
            ],
        ),
    ]
