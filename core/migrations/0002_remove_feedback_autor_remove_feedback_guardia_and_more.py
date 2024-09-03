# Generated by Django 4.2.11 on 2024-08-20 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='guardia',
        ),
        migrations.RemoveField(
            model_name='incidente',
            name='guardia',
        ),
        migrations.RemoveField(
            model_name='miembrocomunidad',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='guardia',
        ),
        migrations.RemoveField(
            model_name='guardia',
            name='activo',
        ),
        migrations.RemoveField(
            model_name='guardia',
            name='fecha_inicio',
        ),
        migrations.AlterField(
            model_name='guardia',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Administrador',
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.DeleteModel(
            name='Incidente',
        ),
        migrations.DeleteModel(
            name='MiembroComunidad',
        ),
        migrations.DeleteModel(
            name='Tarea',
        ),
    ]
