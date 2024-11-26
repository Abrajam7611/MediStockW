import firebase_admin
from firebase_admin import credentials, firestore  # Importa firestore aquí
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from apps.inventario.models import Producto  # Importamos el modelo Producto de Django
from .models import Venta  # Importamos el modelo Venta de Django

# Inicializar Firebase (solo una vez)
if not firebase_admin._apps:
    cred = credentials.Certificate("Clave.json")  # Asegúrate de que 'Clave.json' esté en el directorio correcto
    firebase_admin.initialize_app(cred)

# Función para agregar la venta a Firestore
def agregar_venta(cantidad, fecha, nombre, precio, total):
    # Conectar con Firestore
    db = firestore.client()  # Esta línea usa firestore correctamente

    ventas_ref = db.collection('ventas')

    venta_data = {
        'cantidad': cantidad,
        'fecha': fecha,
        'nombre': nombre,
        'precio': precio,
        'total': total
    }

    # Agregar la venta a Firestore
    ventas_ref.add(venta_data)
    print("Venta agregada exitosamente")

# Vista para crear una venta
def crear_venta(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        cantidad_vendida = int(request.POST.get('cantidad'))
        precio_producto = float(request.POST.get('precio'))

        # Verificar si el producto existe en la base de datos de Django (Inventario)
        try:
            producto = Producto.objects.get(id=producto_id)
            
            # Verificar si hay suficiente stock
            if producto.stock >= cantidad_vendida:
                # 1. Crear la venta en la base de datos de Django
                fecha_actual = timezone.now()
                venta = Venta.objects.create(
                    producto=producto,
                    cantidad=cantidad_vendida,
                    precio=precio_producto,
                    total=cantidad_vendida * precio_producto,
                    fecha=fecha_actual
                )
                
                # 2. Descontar el stock en la base de datos de Django
                producto.stock -= cantidad_vendida
                producto.save()  # Guardar los cambios en el stock
                
                # 3. Actualizar el stock en Firestore
                db = firestore.client()
                productos_ref = db.collection('inventario_producto')
                producto_ref = productos_ref.document(producto_id)
                producto_data = producto_ref.get().to_dict()
                
                # Actualizar el stock en Firestore
                nuevo_stock = producto_data['stock'] - cantidad_vendida
                producto_ref.update({'stock': nuevo_stock})

                # 4. Agregar la venta a Firestore
                agregar_venta(cantidad_vendida, fecha_actual, producto.nombre, precio_producto, cantidad_vendida * precio_producto)
                
                return redirect('mostrar_ventas')  # Redirigir a la vista de ventas
            else:
                return HttpResponse("No hay suficiente stock para completar la venta.")
        except Producto.DoesNotExist:
            return HttpResponse("Producto no encontrado en el inventario.")
    
    return render(request, 'ventas/crear_venta.html')

# Vista para mostrar todas las ventas
def mostrar_ventas(request):
    # Obtener todas las ventas registradas desde Firestore
    db = firestore.client()
    ventas_ref = db.collection('ventas')
    ventas = ventas_ref.stream()

    # Convertir los datos de Firestore en una lista para pasarlos al template
    ventas_list = [venta.to_dict() for venta in ventas]

    return render(request, 'ventas/mostrar_ventas.html', {'ventas': ventas_list})
