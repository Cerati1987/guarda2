from django.urls import path
from .views import DashboardComunidadView

urlpatterns = [
    # otras rutas...
    path('', DashboardComunidadView.as_view(), name='dashboard_comunidad'),
]
