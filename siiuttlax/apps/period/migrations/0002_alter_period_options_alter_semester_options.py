# Generated by Django 5.0.6 on 2024-06-11 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('period', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='period',
            options={'ordering': ['id'], 'verbose_name': 'Periodo', 'verbose_name_plural': 'Periodos'},
        ),
        migrations.AlterModelOptions(
            name='semester',
            options={'ordering': ['id'], 'verbose_name': 'Cuatrimestre', 'verbose_name_plural': 'Cuatrimestres'},
        ),
    ]
