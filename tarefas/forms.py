from django import forms
from .models import Tarefa


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'data_vencimento', 'estado']
        widgets = {
            'data_vencimento': forms.DateInput(attrs={'type': 'date'}),
            'estado': forms.Select(choices=Tarefa.ESTADO_CHOICES),
        }
        labels = {
            'titulo': 'Título',
            'descricao': 'Descrição',
            'data_vencimento': 'Data de Vencimento',
            'estado': 'Estado',
        }
