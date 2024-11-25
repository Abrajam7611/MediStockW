from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    sustancia = models.CharField(max_length=100)
    descripcion = models.TextField()
    lote = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    fecha_caducidad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
