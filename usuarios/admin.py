from django.contrib import admin
from .models import Avatar

# Register your models here.

register_models = [Avatar]
admin.site.register(register_models)

# luego de realizar esto hay que hacer el makemigrations y el migrate
