from django.shortcuts import render, redirect
from .models import Producto

def home(request):
    productos = Producto.objects.all()
    return render(request, "inventarios/product.html", {"productos": productos})

def registrarProducto(request):
    nombre=request.POST['txtNombre']
    sustancia=request.POST['txtSustancia']
    descripcion=request.POST['txtDescripcion']
    lote=request.POST['numLote']
    fecha_caducidad=request.POST['txtFechaDeCaducidad']
    stock=request.POST['numStock']
    precio=request.POST['txtPrecio']

    producto = Producto.objects.create(
        nombre=nombre, sustancia=sustancia, descripcion=descripcion, lote=lote, precio=precio, stock=stock, fecha_caducidad=fecha_caducidad)
    return redirect('/')

def edicionProducto(request, nombre):
    producto = Producto.objects.get(nombre=nombre)
    return render(request, "inventarios/edicionProducto.html", {"nombre":nombre})

def editarProducto(request):
    nombre=request.POST['txtNombre']
    sustancia=request.POST['txtSustancia']
    descripcion=request.POST['txtDescripcion']
    lote=request.POST['numLote']
    fecha_caducidad=request.POST['txtFechaDeCaducidad']
    stock=request.POST['numStock']
    precio=request.POST['txtPrecio']

    producto = Producto.objects.get(nombre=nombre)
    producto.nombre = nombre
    producto.sustancia = sustancia
    producto.descripcion = descripcion
    producto.lote = lote
    producto.fecha_caducidad = fecha_caducidad
    producto.stock = stock
    producto.precio = precio

    producto.save()

    return redirect('/')

def eliminarProducto(request, nombre):
    producto = Producto.objects.filter(nombre=nombre)
    producto.delete()

    return redirect('/')