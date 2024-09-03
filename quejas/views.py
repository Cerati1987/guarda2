from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import messages
from core.models import Queja


class PresentarQuejaView(TemplateView):
    template_name = 'presentar_queja.html'

    def post(self, request, *args, **kwargs):
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        # Crear la instancia de Queja y guardarla
        queja = Queja(
            usuario=request.user,
            nombre=nombre,
            email=email,
            asunto=asunto,
            mensaje=mensaje
        )
        queja.save()

        # Mostrar un mensaje de éxito y redirigir
        messages.success(request, 'Tu queja ha sido enviada exitosamente.')
        return redirect('presentar_queja')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Puedes agregar más contexto si lo necesitas
        return context

from django.views.generic import ListView
from core.models import Queja

class ListarQuejaView(ListView):
    model = Queja
    template_name = 'listar_queja.html'
    context_object_name = 'quejas'
    ordering = ['-fecha_creacion']  # Ordenar por fecha de creación descendente
