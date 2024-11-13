from django.shortcuts import render
from .models import Cliente, Producto

def index(request):
    clientes = Cliente.objects.all()  
    productos = Producto.objects.all()  

    return render(request, 'index.html', {'clientes': clientes, 'productos': productos})
   
"""     if not clientes:
        mensaje_clientes = "No hay clientes registrados."
    else:
        mensaje_clientes = None

    if not productos:
        mensaje_productos = "No hay productos disponibles."
    else:
        mensaje_productos = None

    context = {
        'clientes': clientes,
        'productos': productos,
        'mensaje_clientes': mensaje_clientes,
        'mensaje_productos': mensaje_productos,
    }

    return render(request, 'index.html', context) """
