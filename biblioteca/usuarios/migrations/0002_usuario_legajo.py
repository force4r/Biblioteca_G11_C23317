# Generated by Django 4.2 on 2023-06-13 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='legajo',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]