# apps/inventario/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from firebase_services import obtener_inventario, agregar_producto, actualizar_producto, eliminar_producto

# Vista para mostrar el inventario
def mostrar_inventario(request):
    productos = obtener_inventario()
    return render(request, 'inventario/inventario.html', {'productos': productos})

# Vista para agregar un nuevo producto
def agregar_producto_view(request):
    if request.method == 'POST':
        nuevo_producto = {
            'nombre': request.POST['nombre'],
            'descripcion': request.POST['descripcion'],
            'fecha_caducidad': request.POST['fecha_caducidad'],
            'lote': request.POST['lote'],
            'precio': float(request.POST['precio']),
            'stock': int(request.POST['stock']),
            'sustancia': request.POST['sustancia'],
            'categoria': request.POST['categoria']
        }
        agregar_producto(nuevo_producto)
        return redirect('mostrar_inventario')
    return render(request, 'inventario/agregar_producto.html')

# Vista para editar un producto existente
def editar_producto_view(request, producto_id):
    producto = obtener_inventario().get(producto_id)
    if request.method == 'POST':
        producto_actualizado = {
            'nombre': request.POST['nombre'],
            'descripcion': request.POST['descripcion'],
            'fecha_caducidad': request.POST['fecha_caducidad'],
            'lote': request.POST['lote'],
            'precio': float(request.POST['precio']),
            'stock': int(request.POST['stock']),
            'sustancia': request.POST['sustancia'],
            'categoria': request.POST['categoria']
        }
        actualizar_producto(producto_id, producto_actualizado)
        return redirect('mostrar_inventario')
    return render(request, 'inventario/editar_producto.html', {'producto': producto})

# Vista para eliminar un producto
def eliminar_producto_view(request, producto_id):
    eliminar_producto(producto_id)
    return redirect('mostrar_inventario')
