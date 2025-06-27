from django.urls import path
from . import views

urlpatterns = [
    path('registo/', views.registar, name='registar'),
]
