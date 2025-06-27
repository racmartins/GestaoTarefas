from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rotas da app tarefas (painel, adicionar, editar, etc.)
    path('', include('tarefas.urls')),
    # Rotas personalizadas da app utilizadores (registo)
    path('utilizadores/', include('utilizadores.urls')),
    # Login, logout, alteração de palavra-passe, etc.
    path('accounts/', include('django.contrib.auth.urls')),
]
