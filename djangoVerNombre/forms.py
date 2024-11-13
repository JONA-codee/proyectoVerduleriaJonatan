from django import forms
from .models import Producto, Cliente

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'categoria', 'estado', 'observaciones', 'proveedor']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre_cliente', 'correo', 'telefono', 'direccion', 'ciudad', 'pais', 'tipo_cliente', 'preferencias', 'fecha_nacimiento', 'genero']
