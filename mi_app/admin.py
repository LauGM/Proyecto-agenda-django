from django.contrib import admin
from .models import Contacto, Nota, Tarea

# Register your models here.
models = [Contacto, Nota, Tarea]

for model in models:
    admin.site.register(model)

