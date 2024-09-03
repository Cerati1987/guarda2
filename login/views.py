from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from core.models import Guardia, Administrador, UsuarioComunidad


class CustomLoginView(LoginView):
    template_name = 'login/login.html'

    def get_success_url(self):
        user = self.request.user

        # Verifica si el usuario es un guardia
        if Guardia.objects.filter(user=user).exists():
            return reverse_lazy('home')  # Redirige al dashboard si es un guardia

        # Verifica si el usuario es un administrador
        elif Administrador.objects.filter(user=user).exists():
            return reverse_lazy('dashboard_admin')  # Redirige al dashboard_admin si es un administrador

        # Verifica si el usuario es un usuario de la comunidad
        elif UsuarioComunidad.objects.filter(user=user).exists():
            return reverse_lazy('dashboard_comunidad')  # Redirige al dashboard de la comunidad

        # Redirige a otra página si no es ninguno de los anteriores
        return reverse_lazy('default_home')
