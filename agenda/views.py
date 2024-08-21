from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Agenda
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.paginator import Paginator

class AgendaListView(ListView):
    model = Agenda
    paginate_by = 10

class ProximasReservasView(ListView):
    model = Agenda
    template_name = 'agenda/proximas_reservas.html'
    context_object_name = 'reservas'
    paginate_by = 10

    def get_queryset(self):
        lugar_id = self.kwargs.get('lugar_id')
        return Agenda.objects.filter(lugar_id=lugar_id, fecha__gte=timezone.now()).order_by('fecha', 'hora_comienzo')

class AgendaDetailView(DetailView):
    model = Agenda

class AgendaCreateView(CreateView):
    model = Agenda
    fields = ['persona', 'lugar', 'fecha', 'hora_comienzo', 'hora_final']
    success_url = reverse_lazy('agenda_list')

    def form_valid(self, form):
        lugar = form.cleaned_data['lugar']
        fecha = form.cleaned_data['fecha']
        hora_comienzo = form.cleaned_data['hora_comienzo']
        hora_final = form.cleaned_data['hora_final']
        # Verificar si ya existe una reserva en el mismo horario
        if Agenda.objects.filter(lugar=lugar, fecha=fecha, hora_comienzo__lt=hora_final, hora_final__gt=hora_comienzo).exists():
            form.add_error('hora_comienzo', ValidationError(_('El lugar ya está reservado en este período de tiempo.')))
            return self.form_invalid(form)
        return super().form_valid(form)

class AgendaUpdateView(UpdateView):
    model = Agenda
    fields = ['persona', 'lugar', 'fecha', 'hora_comienzo', 'hora_final']
    success_url = reverse_lazy('agenda_list')

    def form_valid(self, form):
        lugar = form.cleaned_data['lugar']
        fecha = form.cleaned_data['fecha']
        hora_comienzo = form.cleaned_data['hora_comienzo']
        hora_final = form.cleaned_data['hora_final']
        # Mismo chequeo que en CreateView para evitar solapamientos
        if Agenda.objects.filter(lugar=lugar, fecha=fecha, hora_comienzo__lt=hora_final, hora_final__gt=hora_comienzo).exists():
            form.add_error('hora_comienzo', ValidationError(_('El lugar ya está reservado en este período de tiempo.')))
            return self.form_invalid(form)
        return super().form_valid(form)

class AgendaDeleteView(DeleteView):
    model = Agenda
    success_url = reverse_lazy('agenda_list')
