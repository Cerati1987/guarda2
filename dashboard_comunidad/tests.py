from django.test import TestCase
from django.urls import reverse, resolve
from .views import DashboardComunidadView

class DashboardComunidadViewTest(TestCase):

    def test_dashboard_comunidad_view_status_code(self):
        """Verifica que la vista DashboardComunidadView responda con un código 200"""
        response = self.client.get(reverse('dashboard_comunidad'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_comunidad_view_template(self):
        """Verifica que la vista DashboardComunidadView use la plantilla correcta"""
        response = self.client.get(reverse('dashboard_comunidad'))
        self.assertTemplateUsed(response, 'dashboard_comunidad/dashboard_comunidad.html')

    def test_dashboard_comunidad_url_resolves_view(self):
        """Verifica que la URL /dashboard_comunidad/ mapea a DashboardComunidadView"""
        view = resolve('/dashboard_comunidad/')
        self.assertEqual(view.func.view_class, DashboardComunidadView)
