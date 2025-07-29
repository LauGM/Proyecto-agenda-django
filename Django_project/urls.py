"""
URL configuration for Django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from mi_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('crear-contacto/', views.crear_contacto, name='crear-contacto'),
    path('crear-tarea/', views.crear_tarea, name='crear-tarea'),
    path('crear-nota/', views.crear_nota, name='crear-nota'),
    path('buscar-contacto/', views.buscar_contacto, name='buscar-contacto'),
    path('listar-contactos/', views.listar_contactos, name='listar-contactos'),
    path('listar-tareas/', views.listar_tareas, name='listar-tareass'),
    path('listar-notas/', views.listar_notas, name='listar-notas'),
]
