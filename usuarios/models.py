from django.db import models
from django.contrib.auth.models import User

# creo el modelo de avatar y lo relaciono con el user que ya viene en django

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatars/')
    # python -m pip install Pillow
    # hay que agregar algunas cositas en settings.py de Django project para especificar la carpeta /media que guardara la carpeta /avatars

    def __str__(self):
        return f"Avatar de {self.user.username}"