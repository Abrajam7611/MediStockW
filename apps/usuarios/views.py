from django.shortcuts import render, redirect
from django.contrib import messages

from firebase_services import obtener_inventario
from .forms import LoginForm
import firebase_admin
from firebase_admin import credentials, firestore
from django.contrib.auth import login, authenticate

# Inicializar Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate('Clave.json')
    firebase_admin.initialize_app(cred)

db = firestore.Client.from_service_account_json("Clave.json")

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email_address = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                # Buscar el usuario en Firestore por correo electrónico
                query = db.collection('usuarios').where('email', '==', email_address).stream()
                user = None
                for doc in query:
                    user = doc.to_dict()  # Obtener los datos como un diccionario
                    break

                if user and user.get('password') == password:
                    # Usuario autenticado correctamente
                    # Si tu base de datos de Firestore tiene el campo "email", "password" y otros detalles,
                    # puedes crear un objeto de usuario de Django manualmente o redirigir a la página de inicio.
                    
                    # Crear un objeto de usuario en Django (si lo deseas)
                    # Aquí se asume que Firestore tiene los campos 'email' y 'password'
                    user_data = {
                        'email': user['email'],
                        'username': user.get('username', user['email']),  # Usa el email si no hay nombre de usuario
                    }
                    
                    # Aquí solo rediriges a home si se autentica correctamente
                    messages.success(request, "Inicio de sesión exitoso.")
                    return redirect('home')
                else:
                    messages.error(request, "Correo o contraseña incorrectos.")
            except Exception as e:
                messages.error(request, f"Error al conectarse a la base de datos: {e}")
    else:
        form = LoginForm()

    return render(request, 'usuarios/login.html', {'form': form})

def home_view(request):
    # Obtener el inventario desde Firestore
    productos = obtener_inventario()  # Esta función obtiene los productos de la colección 'inventario_producto'
    
    return render(request, 'usuarios/home.html', {'productos': productos})