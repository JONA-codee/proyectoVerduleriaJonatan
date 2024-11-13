from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categoria = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
    observaciones = models.TextField(blank=True, null=True)
    proveedor = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    tipo_cliente = models.CharField(max_length=50)
    preferencias = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre_cliente
