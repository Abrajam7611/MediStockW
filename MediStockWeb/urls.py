from os import path
from django.urls import path, include
# from . import views
from django.contrib import admin # Importamos include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.inventarios.urls')),  # Incluir las URLs de la app 'inventario'
    path('usuarios/', include('apps.usuarios.urls')),
    path('ventas/', include('apps.ventas.urls')),
    # path('reportes/', include('apps.reportes.urls')),
    # path('', views.home, name='home'),

]
