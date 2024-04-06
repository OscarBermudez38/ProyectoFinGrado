from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)  # Usamos EmailField para asegurar que el correo sea válido
    tlf = models.CharField(max_length=9)  
    ciudad = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

class Direccion(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Relación con el modelo Usuario
    calle = models.CharField(max_length=100)
    numero= models.CharField(max_length=10)
    piso = models.IntegerField(blank=True, null=True)
    codigo_postal = models.CharField(max_length=5)
    ciudad = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.piso}, {self.ciudad}, {self.codigo_postal}, {self.pais}"
