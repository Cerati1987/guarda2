from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Queja
from django.contrib.messages import get_messages

class PresentarQuejaViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='usuario_test', password='password123')
        self.client.login(username='usuario_test', password='password123')

    def test_get_presentar_queja_view(self):
        """Verifica que la vista PresentarQuejaView se renderiza correctamente con GET"""
        response = self.client.get(reverse('presentar_queja'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'presentar_queja.html')

    def test_post_presentar_queja_view(self):
        """Verifica que se puede enviar una queja con POST y redirige correctamente"""
        data = {
            'nombre': 'Juan Pérez',
            'email': 'juan.perez@example.com',
            'asunto': 'Problema de seguridad',
            'mensaje': 'El guardia no estaba en su puesto.',
        }
        response = self.client.post(reverse('presentar_queja'), data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('presentar_queja'))
        self.assertTrue(Queja.objects.filter(nombre='Juan Pérez', asunto='Problema de seguridad').exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Tu queja ha sido enviada exitosamente.')


class ListarQuejaViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='usuario_test', password='password123')
        Queja.objects.create(
            usuario=self.user,
            nombre='Juan Pérez',
            email='juan.perez@example.com',
            asunto='Problema de seguridad',
            mensaje='El guardia no estaba en su puesto.',
        )
        self.client.login(username='usuario_test', password='password123')

    def test_get_listar_queja_view(self):
        """Verifica que la vista ListarQuejaView se renderiza correctamente con GET"""
        response = self.client.get(reverse('listar_queja'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listar_queja.html')
        self.assertContains(response, 'Problema de seguridad')
