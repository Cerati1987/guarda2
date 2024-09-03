from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Guardia, Tarea

class ListaTareasViewTest(TestCase):

    def setUp(self):
        # Crear usuario y guardia
        self.user = User.objects.create_user(username='guardia_test', password='password123')
        self.guardia = Guardia.objects.create(user=self.user)
        self.tarea1 = Tarea.objects.create(
            guardia=self.guardia,
            descripcion='Vigilar entrada principal',
            fecha='2024-09-02',
            hora='08:00',
            ubicacion='Entrada principal',
            estado='Pendiente'
        )
        self.tarea2 = Tarea.objects.create(
            guardia=self.guardia,
            descripcion='Ronda nocturna',
            fecha='2024-09-02',
            hora='23:00',
            ubicacion='Planta baja',
            estado='En progreso'
        )
        self.client.login(username='guardia_test', password='password123')

    def test_lista_tareas_view(self):
        """Verifica que la vista ListaTareasView muestra las tareas del guardia actual"""
        response = self.client.get(reverse('lista_tareas'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tareas_asignadas/tareas_asignadas.html')
        self.assertContains(response, 'Vigilar entrada principal')
        self.assertContains(response, 'Ronda nocturna')


class ActualizarEstadoTareaViewTest(TestCase):

    def setUp(self):
        # Crear usuario y guardia
        self.user = User.objects.create_user(username='guardia_test', password='password123')
        self.guardia = Guardia.objects.create(user=self.user)
        self.tarea = Tarea.objects.create(
            guardia=self.guardia,
            descripcion='Vigilar entrada principal',
            fecha='2024-09-02',
            hora='08:00',
            ubicacion='Entrada principal',
            estado='Pendiente'
        )
        self.client.login(username='guardia_test', password='password123')

    def test_actualizar_estado_tarea_view(self):
        """Verifica que se puede actualizar el estado de una tarea"""
        response = self.client.post(reverse('actualizar_estado_tarea', args=[self.tarea.id]), {'estado': 'Completada'})
        self.assertRedirects(response, reverse('lista_tareas'))
        self.tarea.refresh_from_db()
        self.assertEqual(self.tarea.estado, 'Completada')
