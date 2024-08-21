# lugar/admin.py
from django.contrib import admin
from .models import TipoLugar, Lugar

@admin.register(TipoLugar)
class TipoLugarAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)
    search_fields = ('descripcion',)

@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    list_display = ('tipo_lugar', 'numero', 'disponible_ahora')
    search_fields = ('numero',)
    list_filter = ('tipo_lugar', 'disponible_ahora')
