from django.urls import path
from .views import AgendaListView, AgendaDetailView, AgendaCreateView, AgendaUpdateView, AgendaDeleteView, ProximasReservasView

urlpatterns = [
    path('', AgendaListView.as_view(), name='agenda_list'),
    path('<int:pk>/', AgendaDetailView.as_view(), name='agenda_detail'),
    path('nuevo/', AgendaCreateView.as_view(), name='agenda_create'),
    path('<int:pk>/editar/', AgendaUpdateView.as_view(), name='agenda_update'),
    path('<int:pk>/borrar/', AgendaDeleteView.as_view(), name='agenda_delete'),
    path('lugares/<int:lugar_id>/proximas_reservas/', ProximasReservasView.as_view(), name='proximas_reservas'),
]
