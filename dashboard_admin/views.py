from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from core.models import Guardia, Tarea

class Dashboard_AdminView(TemplateView):
    template_name = 'dashboard_admin/dashboard_admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['guardias'] = Guardia.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        guardia_id = request.POST.get('guardia')
        descripcion = request.POST.get('tarea')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        ubicacion = request.POST.get('ubicacion')

        guardia = Guardia.objects.get(id=guardia_id)

        tarea = Tarea(
            guardia=guardia,
            descripcion=descripcion,
            fecha=fecha,
            hora=hora,
            ubicacion=ubicacion
        )
        tarea.save()

        return redirect('dashboard_admin')
