# persona/admin.py
from django.contrib import admin
from .models import TipoPersona, Persona

@admin.register(TipoPersona)
class TipoPersonaAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)
    search_fields = ('descripcion',)

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('tipo_persona', 'apellidos', 'nombres')
    search_fields = ('apellidos', 'nombres')
    list_filter = ('tipo_persona',)
