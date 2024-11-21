# apps/ventas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ventas_inicio, name='ventas_inicio'),  # Ruta principal de ventas
    path('registrar/', views.registrar_venta, name='registrar_venta'),
    path('realizadas/', views.ventas_realizadas, name='ventas_realizadas'),
]
