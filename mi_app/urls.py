from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('new-contact/<str:nombre>/<str:email>/<str:apellido>/', views.new_contact, name='new-contact'),
    path('listar-contactos/', views.listar_contactos, name='listar-contactos'),
    path('crear-contacto/', views.crear_contacto, name='crear-contacto'),
    path('buscar-contacto/', views.buscar_contacto, name='buscar-contacto'),
    path('crear-tarea/', views.crear_tarea, name='crear-tarea'),
    path('crear-nota/', views.crear_nota, name='crear-nota'),
]
