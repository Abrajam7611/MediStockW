from django.shortcuts import render, redirect
from firebase_admin import firestore

# Inicializamos la conexión con Firestore
db = firestore.client()

def home(request):
    # Obtenemos todos los productos desde Firestore
    productos_ref = db.collection('productos')
    productos = {doc.id: doc.to_dict() for doc in productos_ref.stream()}
    return render(request, "inventarios/mostrar_inventario.html", {"productos": productos})

def registrarProducto(request):
    if request.method == 'POST':
        # Obtenemos los datos del formulario
        nombre = request.POST['nombre']
        sustancia = request.POST['sustancia']
        descripcion = request.POST['descripcion']
        lote = request.POST['lote']
        fecha_caducidad = request.POST['fecha_caducidad']
        stock = request.POST['stock']
        precio = request.POST['precio']
        categoria = request.POST['categoria']

        # Preparamos los datos para Firestore
        producto_data = {
            "nombre": nombre,
            "sustancia": sustancia,
            "descripcion": descripcion,
            "lote": lote,
            "fecha_caducidad": fecha_caducidad,
            "stock": int(stock),
            "precio": float(precio),
            "categoria": categoria,
        }

        # Guardamos el producto en Firestore
        db.collection('productos').document(nombre).set(producto_data)
        return redirect('mostrar_inventario')

    return render(request, "inventarios/agregar_producto.html")

def edicionProducto(request, nombre):
    producto_ref = db.collection('productos').document(nombre)
    producto = producto_ref.get()
    if producto.exists:
        return render(request, "inventarios/editar_producto.html", {"producto": producto.to_dict()})
    else:
        return redirect('mostrar_inventario')

def editarProducto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        sustancia = request.POST['sustancia']
        descripcion = request.POST['descripcion']
        lote = request.POST['lote']
        fecha_caducidad = request.POST['fecha_caducidad']
        stock = request.POST['stock']
        precio = request.POST['precio']
        categoria = request.POST['categoria']

        # Actualizamos los datos en Firestore
        producto_ref = db.collection('productos').document(nombre)
        producto_ref.update({
            "sustancia": sustancia,
            "descripcion": descripcion,
            "lote": lote,
            "fecha_caducidad": fecha_caducidad,
            "stock": int(stock),
            "precio": float(precio),
            "categoria": categoria,
        })

        return redirect('mostrar_inventario')

def eliminarProducto(request, nombre):
    # Eliminamos el producto de Firestore
    db.collection('productos').document(nombre).delete()
    return redirect('mostrar_inventario')
