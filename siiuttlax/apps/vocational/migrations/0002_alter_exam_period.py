# Generated by Django 5.0.6 on 2024-07-11 01:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocational', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vocational.stage', verbose_name='Etapa'),
        ),
    ]