from django.urls import path
from .views import PersonaListView, PersonaDetailView, PersonaCreateView, PersonaUpdateView, PersonaDeleteView

urlpatterns = [
    path('', PersonaListView.as_view(), name='persona_list'),
    path('<int:pk>/', PersonaDetailView.as_view(), name='persona_detail'),
    path('nuevo/', PersonaCreateView.as_view(), name='persona_create'),
    path('<int:pk>/editar/', PersonaUpdateView.as_view(), name='persona_update'),
    path('<int:pk>/borrar/', PersonaDeleteView.as_view(), name='persona_delete'),
]
