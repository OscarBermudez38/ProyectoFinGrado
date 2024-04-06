from django.contrib import admin
from .models import MetodoDePago,Pedido,DetallePedido

@admin.register(MetodoDePago)
class MetodoDePagoAdmin(admin.ModelAdmin):
    # Define los campos que deseas mostrar en el panel de administración
    list_display = ('tipo', 'numero_tarjeta', 'fecha_vencimiento', 'codigo_seguridad', 'nombre_titular', 'direccion_facturacion','telefono')
    # Otros ajustes opcionales según tus necesidades

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    # Define los campos que deseas mostrar en el panel de administración
    list_display = ('id_usuario', 'metodo_de_pago', 'direccion_envio', 'total')
    # Otros ajustes opcionales según tus necesidades


@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    # Define los campos que deseas mostrar en el panel de administración
    list_display = ('id_pedido', 'id_producto', 'cantidad','fecha',)
    # Otros ajustes opcionales según tus necesidades
    
