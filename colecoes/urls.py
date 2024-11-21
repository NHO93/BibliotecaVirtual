from django.urls import path
from .views import ColecaoListCreateView, ColecaoDetailView

urlpatterns = [
    path('', ColecaoListCreateView.as_view(), name='colecao-list-create'),
    path('<int:pk>/', ColecaoDetailView.as_view(), name='colecao-detail'),
]
