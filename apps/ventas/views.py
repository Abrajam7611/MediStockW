# apps/ventas/views.py
from django.shortcuts import render

# Vista para el registro de ventas
def registrar_venta(request):
    return render(request, 'ventas/registrar_venta.html')

# Vista para mostrar las ventas realizadas
def ventas_realizadas(request):
    return render(request, 'ventas/ventas_realizadas.html')

# Vista principal de ventas con botones
def ventas_inicio(request):
    return render(request, 'ventas/index.html')
