from django.views.generic import TemplateView, View
from django.shortcuts import redirect, get_object_or_404
from core.models import Tarea, Guardia

class ListaTareasView(TemplateView):
    template_name = 'tareas_asignadas/tareas_asignadas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        guardia = Guardia.objects.get(user=self.request.user)
        context['tareas'] = Tarea.objects.filter(guardia=guardia)
        return context

class ActualizarEstadoTareaView(View):
    def post(self, request, *args, **kwargs):
        tarea_id = kwargs['tarea_id']
        nuevo_estado = request.POST.get('estado')
        tarea = get_object_or_404(Tarea, id=tarea_id, guardia__user=request.user)
        tarea.estado = nuevo_estado
        tarea.save()
        return redirect('lista_tareas')  # Asegúrate de que 'lista_tareas' sea la URL name de tu vista de lista de tareas
