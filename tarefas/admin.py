from django.contrib import admin
from .models import Tarefa


class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'utilizador', 'data_vencimento', 'estado')
    list_filter = ('estado', 'data_vencimento', 'utilizador')
    search_fields = ('titulo', 'descricao')


admin.site.register(Tarefa, TarefaAdmin)
