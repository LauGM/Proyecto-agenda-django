from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.home, name='home'),
    path('new-contact/<str:nombre>/<str:email>/<str:apellido>/', views.new_contact, name='new-contact'),
    path('listar-contactos/', views.listar_contactos, name='listar-contactos'),
    path('crear-contacto/', views.crear_contacto, name='crear-contacto'),
    path('buscar-contacto/', views.buscar_contacto, name='buscar-contacto'),
    path('crear-tarea/', views.crear_tarea, name='crear-tarea'),
    path('listar-tareas/', views.listar_tareas, name='listar-tareas'),

    # Vistas basadas en clases
    path('listar-notas/', views.ListarNotas.as_view(), name='listar-notas'),
    path('crear-nota/', views.CrearNota.as_view(), name='crear-nota'),
    path('editar-nota/<int:pk>', views.EditarNota.as_view(), name='editar-nota'),
    path('eliminar-nota/<int:pk>', views.EliminarNota.as_view(), name='eliminar-nota'),
    path('ver-detalle-nota/<int:pk>', views.VerDetalleNota.as_view(), name='ver-detalle-nota'),
]
