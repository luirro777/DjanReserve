from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personas/', include('persona.urls')),
    path('lugares/', include('lugar.urls')),
    path('agendas/', include('agenda.urls')),
]

