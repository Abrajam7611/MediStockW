# apps/inventario/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_inventario, name='mostrar_inventario'),
    path('agregar_producto/', views.agregar_producto_view, name='agregar_producto'),
    path('editar_producto/<str:producto_id>/', views.editar_producto_view, name='editar_producto'),
    path('eliminar_producto/<str:producto_id>/', views.eliminar_producto_view, name='eliminar_producto'),
]
