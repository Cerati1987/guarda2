from django.urls import path
from .views import Dashboard_AdminView

urlpatterns = [
    path('dashboard_admin/', Dashboard_AdminView.as_view(), name='dashboard_admin'),
]