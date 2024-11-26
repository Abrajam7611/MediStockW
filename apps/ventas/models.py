# apps/ventas/models.py
from django.db import models
from apps.inventario.models import Producto  # Asegúrate de que Producto esté importado correctamente

class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Relación con Producto
    cantidad = models.PositiveIntegerField()  # Solo se permiten cantidades positivas
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio unitario del producto
    total = models.DecimalField(max_digits=10, decimal_places=2)  # Total de la venta (cantidad * precio)
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha de la venta, se asigna automáticamente

    def __str__(self):
        return f"Venta de {self.producto.nombre} - {self.cantidad} unidades"

    # Opcional: Método para calcular el total (aunque lo calculas al momento de crear la venta)
    def calcular_total(self):
        return self.cantidad * self.precio
