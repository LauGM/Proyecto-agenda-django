from django.shortcuts import render
from django.http import HttpResponse
from mi_app.models import Contacto
from mi_app.forms import MiFormulario


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