from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
    
   
class Producto(models.Model):
    
    TALLAS = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]
    
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  # Relación con el modelo Usuario
    nombre = models.CharField(max_length=100)
    imagen= models.ImageField(upload_to='media/productos')
    color = models.CharField(max_length=50)
    talla = models.CharField(max_length=2, choices=TALLAS)
    fecha_salida = models.DateField(auto_now_add=True)
    cantidad = models.CharField(max_length=10)
