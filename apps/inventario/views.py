from django.shortcuts import render

def inventario(request):
    # Aquí puedes obtener el inventario desde la base de datos o definir otros datos
    productos = []  # Este es solo un ejemplo. Asegúrate de obtener tus productos desde la base de datos
    return render(request, 'inventario/inventario.html', {'productos': productos})
