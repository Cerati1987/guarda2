from django.urls import path
from .views import PresentarQuejaView, ListarQuejaView

urlpatterns = [
    path('presentar/', PresentarQuejaView.as_view(), name='presentar_queja'),
    path('listar-quejas/', ListarQuejaView.as_view(), name='listar_queja'),
]
