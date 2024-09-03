from django.urls import path
from .views import HomeView

urlpatterns = [
    path('dashboard/', HomeView.as_view(), name='home'),  # Ruta para la vista principal
]
