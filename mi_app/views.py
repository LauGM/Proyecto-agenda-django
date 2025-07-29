from django.shortcuts import render
from django.http import HttpResponse
from mi_app.models import Contacto, Tarea, Nota
from mi_app.forms import MiFormulario, MiTarea, MiNota


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
            return HttpResponse(f"Contacto creado: {contacto}")

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
            return HttpResponse(f"Tarea creada: {tarea}")

   form = MiTarea()
   return render(request, "mi_app/formularioTarea.html", {"form": form})

def crear_nota(request):
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
            return HttpResponse(f"Nota creada: {nota}")

    form = MiNota()
    return render(request, "mi_app/formularioNota.html", {"form": form})