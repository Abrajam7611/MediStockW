from django.shortcuts import render, redirect
from .forms import VentaForm
from .models import Venta


def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.total = venta.producto.precio * venta.cantidad
            venta.save()
            return redirect('ventas')
    else:
        form = VentaForm()
    return render(request, 'ventas/ventas.html', {'form': form})

def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/lista_ventas.html', {'ventas': ventas})