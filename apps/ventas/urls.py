from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_venta, name='ventas'),
    path('lista/', views.listar_ventas, name='lista_ventas'),
]
