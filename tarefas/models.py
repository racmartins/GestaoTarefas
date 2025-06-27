from django.db import models
from django.contrib.auth.models import User


class Tarefa(models.Model):
    ESTADO_CHOICES = [
        ('pendente', 'Pendente'),
        ('concluida', 'Concluída'),
    ]

    utilizador = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tarefas')
    titulo = models.CharField("Título", max_length=255)
    descricao = models.TextField("Descrição", blank=True, null=True)
    data_vencimento = models.DateField("Data de Vencimento")
    estado = models.CharField("Estado", max_length=10,
                              choices=ESTADO_CHOICES, default='pendente')
    criado_em = models.DateTimeField("Data de Criação", auto_now_add=True)

    def __str__(self):
        return self.titulo
