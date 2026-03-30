from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Persona
from django.core.paginator import Paginator

class PersonaListView(ListView):
    model = Persona
    template_name = 'persona/persona_list.html'
    context_object_name = 'personas'
    paginate_by = 10

    def get_queryset(self):
        return Persona.objects.all().order_by('apellidos', 'nombres')

class PersonaDetailView(DetailView):
    model = Persona

class PersonaCreateView(CreateView):
    model = Persona
    fields = ['tipo_persona', 'apellidos', 'nombres']
    success_url = reverse_lazy('persona_list')

class PersonaUpdateView(UpdateView):
    model = Persona
    fields = ['tipo_persona', 'apellidos', 'nombres']
    success_url = reverse_lazy('persona_list')

class PersonaDeleteView(DeleteView):
    model = Persona
    success_url = reverse_lazy('persona_list')
