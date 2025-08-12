from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegisterForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User


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
