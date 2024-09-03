from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from core.models import UsuarioComunidad

class RegistroViewTest(TestCase):

    def test_get_registro_view(self):
        """Verifica que la vista RegistroView se renderiza correctamente con GET"""
        response = self.client.get(reverse('registro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registro/registro.html')

    def test_post_registro_view_crea_usuario(self):
        """Verifica que se puede registrar un nuevo usuario con POST y redirige correctamente"""
        data = {
            'name': 'Juan Pérez',
            'email': 'juan.perez@example.com',
            'username': 'juanperez',
            'password': 'password123',
        }
        response = self.client.post(reverse('registro'), data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='juanperez').exists())
        self.assertTrue(UsuarioComunidad.objects.filter(user__username='juanperez').exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "La cuenta ha sido creada con éxito. Ahora puedes iniciar sesión.")

    def test_post_registro_view_username_existente(self):
        """Verifica que la vista maneja correctamente cuando el nombre de usuario ya está en uso"""
        User.objects.create_user(username='juanperez', email='juan.perez@example.com', password='password123')
        data = {
            'name': 'Juan Pérez',
            'email': 'juan.perez2@example.com',
            'username': 'juanperez',
            'password': 'password123',
        }
        response = self.client.post(reverse('registro'), data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('registro'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "El nombre de usuario ya está en uso.")

    def test_post_registro_view_email_existente(self):
        """Verifica que la vista maneja correctamente cuando el correo electrónico ya está en uso"""
        User.objects.create_user(username='juanperez2', email='juan.perez@example.com', password='password123')
        data = {
            'name': 'Juan Pérez',
            'email': 'juan.perez@example.com',
            'username': 'juanperez',
            'password': 'password123',
        }
        response = self.client.post(reverse('registro'), data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('registro'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "El correo electrónico ya está en uso.")
