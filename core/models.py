from django.contrib.auth.models import User
from django.db import models

class Guardia(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Incidente(models.Model):
    CATEGORIA_CHOICES = [
        ('Acceso no autorizado', 'Acceso no autorizado'),
        ('Pérdida de datos', 'Pérdida de datos'),
        ('Malware', 'Malware'),
        ('Phishing', 'Phishing'),
        ('Otro', 'Otro'),
    ]

    guardia = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES)
    ubicacion = models.CharField(max_length=255)
    archivos = models.FileField(upload_to='incidentes/', blank=True, null=True)
    fecha_reporte = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Incidente {self.id} - {self.categoria} - {self.guardia.username}"


class Tarea(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En progreso', 'En progreso'),
        ('Completada', 'Completada'),
    ]

    guardia = models.ForeignKey(Guardia, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
    fecha = models.DateField()
    hora = models.TimeField()
    ubicacion = models.CharField(max_length=255)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')


class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

# Añadiendo propiedades al User para saber si es Guardia o Administrador
User.add_to_class('is_guardia', property(lambda u: hasattr(u, 'guardia')))
User.add_to_class('is_administrador', property(lambda u: hasattr(u, 'administrador')))

class UsuarioComunidad(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Queja(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quejas')
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    asunto = models.CharField(max_length=255)
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Queja de {self.nombre} - {self.asunto}"