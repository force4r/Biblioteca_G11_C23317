# Generated by Django 4.2 on 2023-06-20 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_legajo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='dni',
            field=models.BigIntegerField(null=True),
        ),
    ]
