# Generated by Django 4.2.11 on 2024-08-23 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_tarea'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('En progreso', 'En progreso'), ('Completada', 'Completada')], default='Pendiente', max_length=20),
        ),
    ]
