from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}, {self.email}"

class Tarea(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    completada = models.BooleanField(default=False)

    def __str__(self):
        return f'Titulo: {self.titulo},\nDescripcion: {self.descripcion},\nCompletada: {self.completada}'
    
class Nota(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()

    def __str__(self):
        return f'Titulo: {self.titulo},\nContenido: {self.contenido}'