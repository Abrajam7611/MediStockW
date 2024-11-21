from firebase_admin import firestore
from django.shortcuts import render

def lista_productos(request):
    db = firestore.client()  # Inicializa Firestore

    productos_ref = db.collection('productos')  # Referencia a la colección
    documentos = productos_ref.stream()  # Recupera los documentos

    productos = []
    for doc in documentos:
        # Convierte los datos del documento a un diccionario
        datos = doc.to_dict()
        productos.append(datos)

    # Asegúrate de que la plantilla esté en la carpeta correcta
    return render(request, 'inventario/productos_lista.html', {'productos': productos})
