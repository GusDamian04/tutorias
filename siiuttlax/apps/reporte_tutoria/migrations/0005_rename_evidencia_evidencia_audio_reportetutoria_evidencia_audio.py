# Generated by Django 5.0.6 on 2024-07-22 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporte_tutoria', '0004_rename_evidencia4_reportetutoria_evidencia_canalizacion_alumno_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportetutoria',
            old_name='evidencia_evidencia_audio',
            new_name='evidencia_audio',
        ),
    ]
