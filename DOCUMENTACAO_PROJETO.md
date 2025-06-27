# Documentação - Sistema de Gestão de Tarefas Django

## Visão Geral do Projeto

Este é um sistema web de gestão de tarefas desenvolvido em Django que permite aos utilizadores:

- Registar-se e fazer login
- Criar, editar, eliminar e concluir tarefas
- Filtrar e pesquisar tarefas
- Gerir tarefas através de um painel administrativo

## Estrutura do Projeto

```
gestaoTarefa/
├── config/                 # Configurações principais do Django
├── tarefas/               # App principal para gestão de tarefas
├── utilizadores/          # App para gestão de utilizadores
├── templates/             # Templates globais
├── static/               # Arquivos estáticos (CSS, JS, imagens)
├── venv/                 # Ambiente virtual Python
├── db.sqlite3            # Base de dados SQLite
└── manage.py             # Script de gestão do Django
```

## Passo a Passo da Construção

### 1. Configuração Inicial do Ambiente

#### 1.1 Criar e Ativar Ambiente Virtual

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual (macOS/Linux)
source venv/bin/activate

# Ativar ambiente virtual (Windows)
venv\Scripts\activate
```

#### 1.2 Instalar Dependências

```bash
pip install django
pip install django-widget-tweaks  # Para melhor formatação de formulários
```

#### 1.3 Criar Projeto Django

```bash
django-admin startproject config .
```

### 2. Configuração das Settings

#### 2.1 Configurar settings.py

- Definir `BASE_DIR` e `SECRET_KEY`
- Configurar `INSTALLED_APPS` incluindo as apps personalizadas
- Configurar templates globais em `TEMPLATES['DIRS']`
- Definir configurações de base de dados (SQLite para desenvolvimento)
- Configurar arquivos estáticos (`STATIC_URL`, `STATICFILES_DIRS`)
- Definir localização para português (`LANGUAGE_CODE = 'pt-pt'`)
- Configurar redirecionamentos de login/logout

### 3. Criação das Apps

#### 3.1 Criar App Tarefas

```bash
python manage.py startapp tarefas
```

#### 3.2 Criar App Utilizadores

```bash
python manage.py startapp utilizadores
```

#### 3.3 Registar Apps no settings.py

Adicionar 'tarefas' e 'utilizadores' em `INSTALLED_APPS`

### 4. Desenvolvimento da App Tarefas

#### 4.1 Criar Modelo Tarefa (tarefas/models.py)

- Definir campos: titulo, descricao, data_vencimento, estado, criado_em
- Estabelecer relação ForeignKey com User
- Definir choices para estado (pendente/concluida)
- Implementar método `__str__`

#### 4.2 Criar Formulário (tarefas/forms.py)

- Criar `TarefaForm` baseado em ModelForm
- Configurar widgets personalizados (DateInput para data)
- Definir labels em português

#### 4.3 Desenvolver Views (tarefas/views.py)

- `painel`: Listar tarefas do utilizador com filtros
- `adicionar_tarefa`: Criar nova tarefa
- `editar_tarefa`: Editar tarefa existente
- `eliminar_tarefa`: Eliminar tarefa com confirmação
- `concluir_tarefa`: Marcar tarefa como concluída
- Aplicar decorator `@login_required` em todas as views

#### 4.4 Configurar URLs (tarefas/urls.py)

- Definir rotas para todas as views
- Usar parâmetros dinâmicos para ID das tarefas

#### 4.5 Criar Templates

- `painel.html`: Interface principal com lista de tarefas
- `tarefa_form.html`: Formulário para adicionar/editar
- `confirmar_eliminar.html`: Confirmação de eliminação

### 5. Desenvolvimento da App Utilizadores

#### 5.1 Criar Formulário de Registo (utilizadores/forms.py)

- Estender `UserCreationForm`
- Adicionar campo email obrigatório
- Personalizar labels para português

#### 5.2 Criar View de Registo (utilizadores/views.py)

- Implementar função `registar`
- Processar formulário POST
- Redirecionar para login após registo bem-sucedido

#### 5.3 Configurar URLs (utilizadores/urls.py)

- Definir rota para registo

#### 5.4 Criar Template de Registo

- `registo.html`: Formulário de registo de utilizador

### 6. Configuração de Templates Globais

#### 6.1 Criar Template Base (templates/base.html)

- Estrutura HTML base com Bootstrap 5
- Navbar responsiva com links condicionais
- Sistema de autenticação integrado
- Blocos para conteúdo específico

#### 6.2 Criar Templates de Autenticação

- `login.html`: Formulário de login personalizado
- Usar sistema de autenticação built-in do Django

### 7. Configuração de URLs Principais

#### 7.1 Configurar config/urls.py

- Incluir URLs das apps tarefas e utilizadores
- Incluir URLs de autenticação do Django (`django.contrib.auth.urls`)
- Configurar rota para admin

### 8. Configuração do Admin

#### 8.1 Personalizar Admin (tarefas/admin.py)

- Registar modelo Tarefa
- Configurar `TarefaAdmin` com list_display, list_filter, search_fields

#### 8.2 Personalizar Interface Admin (config/admin.py)

- Definir títulos personalizados para interface admin

### 9. Estilização

#### 9.1 Criar Arquivos CSS

- `static/tarefas/styles.css`: Estilos personalizados
- `static/admin/custom.css`: Estilos para admin

#### 9.2 Integrar Bootstrap

- CDN do Bootstrap 5 no template base
- Classes responsivas e componentes modernos

### 10. Migrações e Base de Dados

#### 10.1 Criar e Aplicar Migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 10.2 Criar Superutilizador

```bash
python manage.py createsuperuser
```

### 11. Funcionalidades Implementadas

#### 11.1 Sistema de Autenticação

- Registo de novos utilizadores
- Login/logout
- Proteção de views com `@login_required`

#### 11.2 Gestão de Tarefas

- CRUD completo (Create, Read, Update, Delete)
- Filtros por estado e pesquisa por título
- Marcação rápida como concluída
- Interface responsiva e intuitiva

#### 11.3 Painel Administrativo

- Gestão avançada de tarefas
- Filtros e pesquisa no admin
- Interface personalizada

### 12. Execução do Projeto

#### 12.1 Executar Servidor de Desenvolvimento

```bash
python manage.py runserver
```

#### 12.2 Acessos

- Aplicação principal: http://127.0.0.1:8000/
- Painel administrativo: http://127.0.0.1:8000/admin/
- Registo: http://127.0.0.1:8000/utilizadores/registo/

## Tecnologias Utilizadas

- **Backend**: Django 5.2.3
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Base de Dados**: SQLite (desenvolvimento)
- **Linguagem**: Python
- **Dependências**: django-widget-tweaks

## Estrutura de Ficheiros Principais

- `config/settings.py`: Configurações do projeto
- `tarefas/models.py`: Modelo de dados das tarefas
- `tarefas/views.py`: Lógica de negócio
- `tarefas/forms.py`: Formulários
- `templates/base.html`: Template base
- `static/`: Arquivos CSS e outros recursos estáticos

Este projeto demonstra uma implementação completa de um sistema web Django com autenticação, CRUD operations, interface administrativa e design responsivo.

## Exemplos de Código Principais

### Modelo Tarefa

```python
class Tarefa(models.Model):
    ESTADO_CHOICES = [
        ('pendente', 'Pendente'),
        ('concluida', 'Concluída'),
    ]

    utilizador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tarefas')
    titulo = models.CharField("Título", max_length=255)
    descricao = models.TextField("Descrição", blank=True, null=True)
    data_vencimento = models.DateField("Data de Vencimento")
    estado = models.CharField("Estado", max_length=10, choices=ESTADO_CHOICES, default='pendente')
    criado_em = models.DateTimeField("Data de Criação", auto_now_add=True)
```

### View Principal (Painel)

```python
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
```

### Configuração de URLs

```python
# config/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tarefas.urls')),
    path('utilizadores/', include('utilizadores.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
```

## Comandos Úteis para Desenvolvimento

### Gestão de Migrações

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Ver migrações
python manage.py showmigrations
```

### Gestão de Utilizadores

```bash
# Criar superutilizador
python manage.py createsuperuser

# Alterar palavra-passe de utilizador
python manage.py changepassword <username>
```

### Desenvolvimento

```bash
# Executar servidor
python manage.py runserver

# Executar shell Django
python manage.py shell

# Recolher arquivos estáticos (produção)
python manage.py collectstatic
```

## Melhorias Futuras Sugeridas

1. **Notificações**: Sistema de alertas para tarefas próximas do vencimento
2. **Categorias**: Organização de tarefas por categorias/projetos
3. **Anexos**: Possibilidade de anexar ficheiros às tarefas
4. **API REST**: Implementar API para integração com outras aplicações
5. **Testes**: Adicionar testes unitários e de integração
6. **Deploy**: Configuração para produção com PostgreSQL e servidor web
7. **Responsividade**: Melhorar interface mobile
8. **Relatórios**: Dashboard com estatísticas de produtividade

## Estrutura de Segurança

- Autenticação obrigatória para todas as funcionalidades
- Isolamento de dados por utilizador
- Proteção CSRF em formulários
- Validação de permissões nas views
- Configurações de segurança do Django ativas
