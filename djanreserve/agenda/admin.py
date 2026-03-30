# agenda/admin.py
from django.contrib import admin
from .models import Agenda
from .forms import AgendaAdminForm

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    form = AgendaAdminForm
    list_display = ('persona', 'lugar', 'fecha', 'hora_comienzo', 'hora_final')
    search_fields = ('persona__nombres', 'lugar__numero')
    list_filter = ('fecha', 'hora_comienzo', 'hora_final')
    ordering = ('-fecha', 'hora_comienzo')
