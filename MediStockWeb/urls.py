from django.contrib import admin
from django.urls import path, include  # Importamos include
from apps.usuarios import views  # Importamos las vistas desde la app usuarios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),  # Ruta de la página de inicio
    path('login', views.login_view, name='login'),  # Ruta principal para login
    path('ventas/', include('apps.ventas.urls')),
    path('inventarios/', include('apps.inventarios.urls')),  # Incluir las URLs de la app 'inventario'
    path('usuarios/', include('apps.usuarios.urls')),

]
