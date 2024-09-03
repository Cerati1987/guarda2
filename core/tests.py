from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Guardia, Incidente, Tarea, Administrador, UsuarioComunidad, Queja

class GuardiaModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='guardia_test', password='password123')
        self.guardia = Guardia.objects.create(user=self.user)

    def test_guardia_str(self):
        self.assertEqual(str(self.guardia), 'guardia_test')


class IncidenteModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='guardia_test', password='password123')
        self.incidente = Incidente.objects.create(
            guardia=self.user,
            descripcion='Descripción del incidente',
            categoria='Malware',
            ubicacion='Oficina',
        )

    def test_incidente_str(self):
        self.assertEqual(
            str(self.incidente),
            f"Incidente {self.incidente.id} - Malware - guardia_test"
        )


class TareaModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='guardia_test', password='password123')
        self.guardia = Guardia.objects.create(user=self.user)
        self.tarea = Tarea.objects.create(
            guardia=self.guardia,
            descripcion='Patrullaje nocturno',
            fecha='2024-09-01',
            hora='23:00',
            ubicacion='Zona 1',
            estado='Pendiente',
        )

    def test_tarea_estado_default(self):
        self.assertEqual(self.tarea.estado, 'Pendiente')


class AdministradorModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin_test', password='password123')
        self.administrador = Administrador.objects.create(user=self.user)

    def test_administrador_str(self):
        self.assertEqual(str(self.administrador), 'admin_test')


class UsuarioComunidadModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='comunidad_test', password='password123')
        self.usuario_comunidad = UsuarioComunidad.objects.create(user=self.user)

    def test_usuario_comunidad_str(self):
        self.assertEqual(str(self.usuario_comunidad), 'comunidad_test')


class QuejaModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='usuario_test', password='password123')
        self.queja = Queja.objects.create(
            usuario=self.user,
            nombre='Juan Pérez',
            email='juan.perez@example.com',
            asunto='Problema con la seguridad',
            mensaje='El guardia no estaba presente en su puesto de trabajo.',
        )

    def test_queja_str(self):
        self.assertEqual(
            str(self.queja),
            "Queja de Juan Pérez - Problema con la seguridad"
        )
