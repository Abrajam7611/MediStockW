from django.urls import path
from .views import registrar_venta, listar_ventas
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.mostrar_ventas, name='mostrar_ventas'),  # Ruta raíz que muestra las ventas
    path('crear/', views.crear_venta, name='crear_venta'),  # Ruta para crear una venta
=======
    path('registrar/', views.registrar_venta, name='ventas'),
    path('lista/', views.listar_ventas, name='lista_ventas'),
>>>>>>> 9c5a97c89a3e0727a38c4432c6d161dccc41a9a0
]
