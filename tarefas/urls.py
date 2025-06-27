from django.urls import path
from . import views

urlpatterns = [
    path('', views.painel, name='painel'),
    path('adicionar/', views.adicionar_tarefa, name='adicionar_tarefa'),
    path('editar/<int:tarefa_id>/', views.editar_tarefa, name='editar_tarefa'),
    path('eliminar/<int:tarefa_id>/',
         views.eliminar_tarefa, name='eliminar_tarefa'),
    path('concluir/<int:tarefa_id>/',
         views.concluir_tarefa, name='concluir_tarefa'),
]
