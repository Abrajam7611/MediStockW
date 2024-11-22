from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventario, name='inventario'),  # Aquí debe ser la misma vista que definiste en views.py
]
