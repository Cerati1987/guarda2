from django.urls import path
from .views import RegistroIncidenteView, ListaIncidentesView

urlpatterns = [
    path('registro/', RegistroIncidenteView.as_view(), name='registro_incidente'),
    path('incidentes_reportados/', ListaIncidentesView.as_view(), name='incidentes_reportados'),
]
