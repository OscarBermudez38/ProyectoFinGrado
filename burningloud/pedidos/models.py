from django.db import models
from usuarios.models import Usuario
from productos.models import Producto


# Create your models here.

class MetodoDePago(models.Model):
    TIPO_PAGO = [
        ('TC', 'Tarjeta de crédito'),
        ('TD', 'Tarjeta de débito'),
    ]

    tipo = models.CharField(max_length=10, choices=TIPO_PAGO)
    numero_tarjeta = models.CharField(max_length=16)
    fecha_vencimiento = models.DateField()
    codigo_seguridad = models.CharField(max_length=4)
    nombre_titular = models.CharField(max_length=100)
    direccion_facturacion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)

class Pedido(models.Model):
    
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Relación con el modelo Usuario
    metodo_de_pago = models.ForeignKey(MetodoDePago, on_delete=models.CASCADE)  # Relación con el modelo Usuario
    direccion_envio = models.CharField(max_length=200, default="Direccion predeterminada")
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
class DetallePedido(models.Model):
    
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)  # Relación con el modelo Usuario
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Relación con el modelo Usuario
    cantidad = models.CharField(max_length=10)
    fecha = models.DateField()
