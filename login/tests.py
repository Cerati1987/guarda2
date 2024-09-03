from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from core.models import Guardia, Administrador, UsuarioComunidad

class CustomLoginViewTest(TestCase):

    def setUp(self):
        self.guard_user = User.objects.create_user(username='guardia_test', password='password123')
        self.admin_user = User.objects.create_user(username='admin_test', password='password123')
        self.community_user = User.objects.create_user(username='comunidad_test', password='password123')

        Guardia.objects.create(user=self.guard_user)
        Administrador.objects.create(user=self.admin_user)
        UsuarioComunidad.objects.create(user=self.community_user)

    def test_login_redirects_guardia(self):
        """Verifica que un guardia sea redirigido al dashboard de guardias"""
        response = self.client.post(reverse('login'), {'username': 'guardia_test', 'password': 'password123'})
        self.assertRedirects(response, reverse('home'))

    def test_login_redirects_administrador(self):
        """Verifica que un administrador sea redirigido al dashboard de administradores"""
        response = self.client.post(reverse('login'), {'username': 'admin_test', 'password': 'password123'})
        self.assertRedirects(response, reverse('dashboard_admin'))

    def test_login_redirects_usuario_comunidad(self):
        """Verifica que un usuario de la comunidad sea redirigido al dashboard de la comunidad"""
        response = self.client.post(reverse('login'), {'username': 'comunidad_test', 'password': 'password123'})
        self.assertRedirects(response, reverse('dashboard_comunidad'))

    def test_login_url_resolves_login_view(self):
        """Verifica que la URL /login/ resuelve a la vista CustomLoginView"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login.html')
