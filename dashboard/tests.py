from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from .views import HomeView

class HomeViewTest(TestCase):

    def test_home_view_status_code(self):
        """Verifica que la vista HomeView responda con un código 200"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_template(self):
        """Verifica que la vista HomeView use la plantilla correcta"""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'dashboard/dashboard.html')

    def test_home_url_resolves_home_view(self):
        """Verifica que la URL /dashboard/ mapea a HomeView"""
        view = resolve('/dashboard/')
        self.assertEqual(view.func.view_class, HomeView)
