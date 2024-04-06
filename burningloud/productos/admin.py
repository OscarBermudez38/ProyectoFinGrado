from django.contrib import admin
from .models import Categoria,Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    # Define los campos que deseas mostrar en el panel de administración
    list_display = ('nombre', 'slug', 'descripcion')
    # Otros ajustes opcionales según tus necesidades
    
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Define los campos que deseas mostrar en el panel de administración
    list_display = ('id_categoria', 'nombre', 'imagen', 'color', 'talla', 'fecha_salida','cantidad')
    # Otros ajustes opcionales según tus necesidades
