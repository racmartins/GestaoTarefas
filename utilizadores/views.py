from django.shortcuts import render, redirect
from .forms import RegistoForm


def registar(request):
    if request.method == 'POST':
        form = RegistoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistoForm()
    return render(request, 'utilizadores/registo.html', {'form': form})
