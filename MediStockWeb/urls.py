from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ventas/', include('apps.ventas.urls')),
    path('productos/', include('apps.inventario.urls')), 
]
