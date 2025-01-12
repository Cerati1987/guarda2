# Generated by Django 4.2.11 on 2024-08-24 04:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_tarea_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incidente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('categoria', models.CharField(choices=[('Acceso no autorizado', 'Acceso no autorizado'), ('Pérdida de datos', 'Pérdida de datos'), ('Malware', 'Malware'), ('Phishing', 'Phishing'), ('Otro', 'Otro')], max_length=50)),
                ('ubicacion', models.CharField(max_length=255)),
                ('archivos', models.FileField(blank=True, null=True, upload_to='incidentes/')),
                ('fecha_reporte', models.DateTimeField(auto_now_add=True)),
                ('guardia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
