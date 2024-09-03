from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),  # Vista de inicio de sesión
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # Vista de cierre de sesión
]
