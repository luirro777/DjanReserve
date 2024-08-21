from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Lugar
from django.core.paginator import Paginator


class LugarListView(ListView):
    model = Lugar
    template_name = 'lugar/lugar_list.html'
    context_object_name = 'lugares'
    paginate_by = 10

    def get_queryset(self):
        return Lugar.objects.all().order_by('tipo_lugar__descripcion', 'numero')  # Ordena por 'tipo_lugar' y 'numero'

class LugarDetailView(DetailView):
    model = Lugar

class LugarCreateView(CreateView):
    model = Lugar
    fields = ['tipo_lugar', 'numero', 'disponible_ahora']
    success_url = reverse_lazy('lugar_list')

class LugarUpdateView(UpdateView):
    model = Lugar
    fields = ['tipo_lugar', 'numero', 'disponible_ahora']
    success_url = reverse_lazy('lugar_list')

class LugarDeleteView(DeleteView):
    model = Lugar
    success_url = reverse_lazy('lugar_list')
