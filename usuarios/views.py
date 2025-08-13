from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegisterForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Avatar


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'usuarios/register.html'
    success_url = reverse_lazy('login')

# login
class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'
    form_class = LoginForm
    # success_url = reverse_lazy('home')
    def get_success_url(self):
        return reverse_lazy('home')

# logout
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

# profile
class ProfileView(DetailView):
    model = User
    template_name = 'usuarios/profile.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user

class AvatarUpdateView(UpdateView):
    model = Avatar
    fields = ['imagen'] 
    # imagen viene del modelo
    template_name = 'usuarios/avatar_form.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self):
        # obtiene o crea el avatar asociado al usuario actual
        avatar, created = Avatar.objects.get_or_create(user=self.request.user)
        return avatar