# MediStockWeb/urls.py

from django.contrib import admin
from django.urls import path, include  # Importamos include
from apps.usuarios import views  # Importamos las vistas desde la app usuarios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),  # Ruta principal para login
    path('home/', views.home_view, name='home'),  # Ruta de la página de inicio
]
