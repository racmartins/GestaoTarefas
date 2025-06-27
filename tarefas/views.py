from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tarefa
from .forms import TarefaForm


@login_required
def painel(request):
    tarefas = Tarefa.objects.filter(utilizador=request.user)
    pesquisa = request.GET.get('pesquisa')
    estado = request.GET.get('estado')
    if pesquisa:
        tarefas = tarefas.filter(titulo__icontains=pesquisa)
    if estado:
        tarefas = tarefas.filter(estado=estado)
    return render(request, 'tarefas/painel.html', {'tarefas': tarefas})


@login_required
def adicionar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.utilizador = request.user
            tarefa.save()
            return redirect('painel')
    else:
        form = TarefaForm()
    return render(request, 'tarefas/tarefa_form.html', {'form': form, 'titulo_form': 'Adicionar Tarefa'})


@login_required
def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id, utilizador=request.user)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('painel')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'tarefas/tarefa_form.html', {'form': form, 'titulo_form': 'Editar Tarefa'})


@login_required
def eliminar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id, utilizador=request.user)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('painel')
    return render(request, 'tarefas/confirmar_eliminar.html', {'tarefa': tarefa})


@login_required
def concluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id, utilizador=request.user)
    tarefa.estado = 'concluida'
    tarefa.save()
    return redirect('painel')
