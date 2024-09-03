from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from core.models import UsuarioComunidad


class RegistroView(View):
    template_name = 'registro/registro.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verificar si el usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
            return redirect('registro')

        if User.objects.filter(email=email).exists():
            messages.error(request, "El correo electrónico ya está en uso.")
            return redirect('registro')

        # Crear el usuario
        user = User.objects.create_user(username=username, email=email, password=password, first_name=name)

        # Crear el perfil de UsuarioComunidad
        UsuarioComunidad.objects.create(user=user)

        messages.success(request, "La cuenta ha sido creada con éxito. Ahora puedes iniciar sesión.")
        return redirect('login')
