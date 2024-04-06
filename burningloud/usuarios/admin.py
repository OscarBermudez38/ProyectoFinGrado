from django.contrib import admin
from .models import Usuario,Direccion  # Importa el modelo Usuario desde tu aplicación

# Define una clase de administración para el modelo Usuario
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    # Define los campos que deseas mostrar en el panel de administración
    list_display = ('nombre', 'apellidos', 'correo', 'tlf', 'ciudad', 'pais')
    # Otros ajustes opcionales según tus necesidades
    
@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    # Define los campos que deseas mostrar en el panel de administración
    list_display = ('id_usuario', 'calle', 'numero', 'piso', 'codigo_postal', 'ciudad','pais')
    # Otros ajustes opcionales según tus necesidades
