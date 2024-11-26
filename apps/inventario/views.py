from django.shortcuts import render, redirect
from firebase_admin import firestore

db = firestore.client()  

def home(request):
    productos_ref = db.collection('productos')
    productos = [doc.to_dict() for doc in productos_ref.stream()]
    return render(request, "product.html", {"productos": productos})

def registrarProducto(request):
    nombre = request.POST['txtNombre']
    sustancia = request.POST['txtSustancia']
    descripcion = request.POST['txtDescripcion']
    lote = request.POST['numLote']
    fecha_caducidad = request.POST['txtFechaDeCaducidad']
    stock = request.POST['numStock']
    precio = request.POST['txtPrecio']

    producto_data = {
        "nombre": nombre,
        "sustancia": sustancia,
        "descripcion": descripcion,
        "lote": lote,
        "fecha_caducidad": fecha_caducidad,
        "stock": int(stock),
        "precio": float(precio),
    }

    db.collection('productos').document(nombre).set(producto_data)
    return redirect('/inventario/')

def edicionProducto(request, nombre):
    producto_ref = db.collection('productos').document(nombre)
    producto = producto_ref.get()
    if producto.exists:
        return render(request, "edicionProducto.html", {"producto": producto.to_dict()})
    else:
        return redirect('/inventario/')

def editarProducto(request):
    nombre = request.POST['txtNombre']
    sustancia = request.POST['txtSustancia']
    descripcion = request.POST['txtDescripcion']
    lote = request.POST['numLote']
    fecha_caducidad = request.POST['txtFechaDeCaducidad']
    stock = request.POST['numStock']
    precio = request.POST['txtPrecio']

    producto_ref = db.collection('productos').document(nombre)
    producto_ref.update({
        "sustancia": sustancia,
        "descripcion": descripcion,
        "lote": lote,
        "fecha_caducidad": fecha_caducidad,
        "stock": int(stock),
        "precio": float(precio),
    })

    return redirect('/inventario/')

def eliminarProducto(request, nombre):
    db.collection('productos').document(nombre).delete()
    return redirect('/inventario/')
