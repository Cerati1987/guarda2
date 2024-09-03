from django.urls import path
from .views import RegistroView

urlpatterns = [
    path('', RegistroView.as_view(), name='registro'),
]