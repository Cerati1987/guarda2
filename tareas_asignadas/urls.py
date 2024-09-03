from django.urls import path
from .views import ListaTareasView, ActualizarEstadoTareaView

urlpatterns = [
    path('lista_tareas/', ListaTareasView.as_view(), name='lista_tareas'),
    path('tarea/<int:tarea_id>/actualizar_estado/', ActualizarEstadoTareaView.as_view(),
         name='actualizar_estado_tarea'),
]
