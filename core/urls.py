from django.urls import path
from core.views import index, AcaoCreate, Index, AcaoUpdate, deletar

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('adicionar/', AcaoCreate.as_view(), name='add'),
    path('editar/<int:pk>/', AcaoUpdate.as_view(), name='editar'),
    path('deletar/<int:pk>/', deletar, name='deletar'),
]