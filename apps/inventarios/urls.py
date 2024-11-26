from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='mostrar_inventario'),
    path('agregar/', views.registrarProducto, name='agregar_producto'),
    path('editar/<str:nombre>/', views.edicionProducto, name='editar_producto'),
    path('editar_producto/', views.editarProducto, name='guardar_edicion_producto'),
    path('eliminar/<str:nombre>/', views.eliminarProducto, name='eliminar_producto'),
]
