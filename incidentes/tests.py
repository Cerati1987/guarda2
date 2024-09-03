from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Incidente, Administrador, Guardia
from django.core.files.uploadedfile import SimpleUploadedFile

class RegistroIncidenteViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='guardia_test', password='password123')
        Guardia.objects.create(user=self.user)
        self.client.login(username='guardia_test', password='password123')

    def test_get_registro_incidente_view(self):
        """Verifica que la vista RegistroIncidenteView se renderiza correctamente con GET"""
        response = self.client.get(reverse('registro_incidente'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'incidentes/registro_incidentes.html')

    def test_post_registro_incidente_view(self):
        """Verifica que se puede registrar un incidente con POST y redirige correctamente"""
        uploaded_file = SimpleUploadedFile('test_image.jpg', b'file_content', content_type='image/jpeg')
        data = {
            'incidentDescription': 'Descripción del incidente',
            'incidentCategory': 'Malware',
            'incidentLocation': 'Oficina',
            'incidentMedia': [uploaded_file],
        }
        response = self.client.post(reverse('registro_incidente'), data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('registro_incidente'))
        self.assertTrue(Incidente.objects.filter(descripcion='Descripción del incidente').exists())


class ListaIncidentesViewTest(TestCase):

    def setUp(self):
        self.admin_user = User.objects.create_user(username='admin_test', password='password123')
        Administrador.objects.create(user=self.admin_user)
        self.guardia_user = User.objects.create_user(username='guardia_test', password='password123')
        Guardia.objects.create(user=self.guardia_user)

    def test_get_lista_incidentes_view_as_admin(self):
        """Verifica que la vista ListaIncidentesView se renderiza correctamente para el administrador"""
        self.client.login(username='admin_test', password='password123')
        response = self.client.get(reverse('incidentes_reportados'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'incidentes/incidentes_reportados.html')

    def test_get_lista_incidentes_view_as_guardia(self):
        """Verifica que la vista ListaIncidentesView redirige a home si el usuario no es administrador"""
        self.client.login(username='guardia_test', password='password123')
        response = self.client.get(reverse('incidentes_reportados'))
        self.assertRedirects(response, reverse('home'))

    def test_lista_incidentes_view_file_type_classification(self):
        """Verifica que la clasificación de archivos en la lista de incidentes funciona correctamente"""
        self.client.login(username='admin_test', password='password123')
        incidente = Incidente.objects.create(
            guardia=self.guardia_user,
            descripcion='Incidente con imagen',
            categoria='Malware',
            ubicacion='Oficina',
        )
        uploaded_file = SimpleUploadedFile('test_image.jpg', b'file_content', content_type='image/jpeg')
        incidente.archivos.save(uploaded_file.name, uploaded_file)
        incidente.save()

        response = self.client.get(reverse('incidentes_reportados'))
        self.assertEqual(response.status_code, 200)
        incidentes = response.context['incidentes']
        self.assertEqual(incidentes[0].tipo_archivo, 'imagen')
