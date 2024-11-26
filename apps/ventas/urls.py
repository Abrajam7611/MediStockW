from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_ventas, name='mostrar_ventas'),  # Ruta raíz que muestra las ventas
    path('crear/', views.crear_venta, name='crear_venta'),  # Ruta para crear una venta
]
