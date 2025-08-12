from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from mi_app.models import Contacto, Tarea, Nota
from mi_app.forms import MiFormulario, MiTarea, MiNota
#nuevo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the mi_app index.")


def home(request):
    return render(request, "mi_app/home.html")


def new_contact(request, nombre, email, apellido):
    if nombre and email and apellido:
        contacto = Contacto.objects.create(
            nombre=nombre,
            email=email,
            apellido=apellido,
        )
    return render(request, "mi_app/new_contact.html", {"contacto": contacto})


def listar_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, "mi_app/listar_contactos.html", {"contactos": contactos})


def crear_contacto(request):
    if request.method == "POST":
        form = MiFormulario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            email = form.cleaned_data["email"]
            contacto = Contacto.objects.create(
                nombre=nombre,
                apellido=apellido,
                email=email,
            )
            contacto.save()
            messages.success(request, f"¡Nota '{contacto.nombre} {contacto.apellido}' creado con éxito!")
            return redirect('crear-contacto')

    form = MiFormulario()
    return render(request, "mi_app/fromulario.html", {"form": form})

def buscar_contacto(request):
    if request.method == "GET":
        nombre = request.GET.get("nombre")
        contactos = Contacto.objects.filter(nombre__contains=nombre)
        return render(request, "mi_app/listar_contactos.html", {"contactos": contactos})
    

def crear_tarea(request):
   if request.method == "POST":
        form = MiTarea(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data["titulo"]
            descripcion = form.cleaned_data["descripcion"]
            completada = form.cleaned_data["completada"]
            tarea = Tarea.objects.create(
                titulo=titulo,
                descripcion=descripcion,
                completada=completada,
            )
            tarea.save()
            messages.success(request, f"¡Tarea '{tarea.titulo}' creada con éxito!")
            return redirect('crear-tarea')

   form = MiTarea()
   return render(request, "mi_app/formularioTarea.html", {"form": form})


def listar_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, "mi_app/listar_tareas.html", {"tareas": tareas})

""" def crear_nota(request):
    if request.method == "POST":
        form = MiNota(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data["titulo"]
            contenido = form.cleaned_data["contenido"]
            nota = Nota.objects.create(
                titulo=titulo,
                contenido=contenido,
            )
            nota.save()
            messages.success(request, f"¡Nota '{nota.titulo}' creada con éxito!")
            return redirect('crear-nota')

    form = MiNota()
    return render(request, "mi_app/formularioNota.html", {"form": form}) """

""" 

def listar_notas(request):
    notas = Nota.objects.all()
    return render(request, "mi_app/listar_notas.html", {"notas": notas}) """

# Vistas basadas en clases

class ListarNotas(ListView):
    model = Nota
    template_name = 'mi_app/listar_notas.html'
    context_object_name = 'notas'

class CrearNota(CreateView):
    model = Nota
    form_class = MiNota
    template_name = 'mi_app/formularioNota.html'
    # si quiero redireccionar despues de crear la nota 
    success_url = reverse_lazy('listar-notas')

class EditarNota(UpdateView):
    model = Nota
    form_class = MiNota
    template_name = 'mi_app/formularioNota.html'
    context_object_name = 'nota'
    success_url = reverse_lazy('listar-notas')

class EliminarNota(DeleteView):
    model = Nota
    template_name = 'mi_app/eliminar_nota.html'
    context_object_name = 'nota'
    success_url = reverse_lazy('listar-notas')

class VerDetalleNota(DetailView):
    model = Nota
    template_name = 'mi_app/ver_detalle_nota.html'
    context_object_name = 'nota'