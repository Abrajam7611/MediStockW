# apps/ventas/views.py
from django.shortcuts import render

# Vista principal de ventas con botones
def ventas_inicio(request):
    return render(request, 'ventas/ventas.html')
