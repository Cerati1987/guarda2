from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'dashboard/dashboard.html'  # Aquí especificas el nombre de la plantilla que quieres renderizar
