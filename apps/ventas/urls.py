# apps/ventas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ventas_inicio, name='ventas_inicio'),  # Ruta principal de ventas
]
