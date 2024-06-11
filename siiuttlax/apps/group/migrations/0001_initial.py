# Generated by Django 5.0.6 on 2024-06-11 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academy', '0001_initial'),
        ('career', '0001_initial'),
        ('period', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F'), ('G', 'G'), ('H', 'H')], default='A', max_length=1)),
                ('observations', models.CharField(blank=True, max_length=50, null=True, verbose_name='Observaciones')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.career')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='period.period')),
                ('semester', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='period.semester')),
                ('tutor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academy.professor')),
            ],
            options={
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
                'ordering': ['group'],
            },
        ),
    ]
