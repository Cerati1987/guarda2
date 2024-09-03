from django.shortcuts import render, redirect
from django.views import View
from core.models import Incidente
from django.contrib.auth.mixins import LoginRequiredMixin

class RegistroIncidenteView(LoginRequiredMixin, View):
    template_name = "incidentes/registro_incidentes.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        descripcion = request.POST.get('incidentDescription')
        categoria = request.POST.get('incidentCategory')
        ubicacion = request.POST.get('incidentLocation')
        archivos = request.FILES.getlist('incidentMedia')

        incidente = Incidente(
            guardia=request.user,
            descripcion=descripcion,
            categoria=categoria,
            ubicacion=ubicacion,
        )
        incidente.save()

        for archivo in archivos:
            incidente.archivos.save(archivo.name, archivo)

        return redirect('registro_incidente')  # Redirige después de guardar

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Incidente

class ListaIncidentesView(LoginRequiredMixin, View):
    template_name = "incidentes/incidentes_reportados.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_administrador:
            incidentes = Incidente.objects.all()
            for incidente in incidentes:
                if incidente.archivos:
                    if incidente.archivos.url.lower().endswith(('.jpg', '.jpeg', '.png')):
                        incidente.tipo_archivo = 'imagen'
                    elif incidente.archivos.url.lower().endswith(('.mp4', '.mov', '.avi')):
                        incidente.tipo_archivo = 'video'
                    else:
                        incidente.tipo_archivo = 'otro'
                else:
                    incidente.tipo_archivo = None
            return render(request, self.template_name, {'incidentes': incidentes})
        else:
            return redirect('home')

