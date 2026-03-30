from django.urls import path
from .views import LugarListView, LugarDetailView, LugarCreateView, LugarUpdateView, LugarDeleteView

urlpatterns = [
    path('', LugarListView.as_view(), name='lugar_list'),
    path('<int:pk>/', LugarDetailView.as_view(), name='lugar_detail'),
    path('nuevo/', LugarCreateView.as_view(), name='lugar_create'),
    path('<int:pk>/editar/', LugarUpdateView.as_view(), name='lugar_update'),
    path('<int:pk>/borrar/', LugarDeleteView.as_view(), name='lugar_delete'),
]
