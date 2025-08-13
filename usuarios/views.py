from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import View
from .forms import RegisterForm, LoginForm, UserUpdateForm, AvatarUpdateForm, CustomPasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Avatar
from django.contrib.auth.mixins import LoginRequiredMixin
# securiza los accesos
from django.contrib.auth import update_session_auth_hash
# update_session_auth_hash actualiza la sesion del usuario


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
class ProfileView(LoginRequiredMixin,DetailView):
    # LoginRequiredMixin se asegura que el usuario este autenticado y debe ir siempre primero
    # sirve para vistas basadas en clases solo
    model = User
    template_name = 'usuarios/profile.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user

class AvatarUpdateView(LoginRequiredMixin, UpdateView):
    model = Avatar
    fields = ['imagen'] 
    # imagen viene del modelo
    template_name = 'usuarios/avatar_form.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self):
        # obtiene o crea el avatar asociado al usuario actual
        avatar, created = Avatar.objects.get_or_create(user=self.request.user)
        return avatar


class ProfileUpdateView(LoginRequiredMixin, View):
    template_name = 'usuarios/profile_update_form.html'
    success_url = reverse_lazy('profile')

    def get(self, request, *args, **kwargs):
        # Usamos get_or_create para asegurarnos de que el avatar exista y que de movida le pase el avatar por defecto que de encuentra en la carpeta /media/avatars
        avatar, _ = Avatar.objects.get_or_create(user=request.user)
        user_form = UserUpdateForm(instance=request.user)
        avatar_form = AvatarUpdateForm(instance=avatar)
        password_form = CustomPasswordChangeForm(user=request.user)
        
        context = {
            'user_form': user_form,
            'avatar_form': avatar_form,
            'password_form': password_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # Usamos get_or_create para asegurarnos de que el avatar exista
        avatar, _ = Avatar.objects.get_or_create(user=request.user)
        user_form = UserUpdateForm(request.POST, instance=request.user)
        avatar_form = AvatarUpdateForm(request.POST, request.FILES, instance=avatar)
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)

        if 'update_profile' in request.POST:
            if user_form.is_valid() and avatar_form.is_valid():
                user_form.save()
                avatar_form.save()
                return redirect(self.success_url)
            else:
                context = {
                    'user_form': user_form,
                    'avatar_form': avatar_form,
                    'password_form': CustomPasswordChangeForm(user=request.user),
                }
                return render(request, self.template_name, context)

        elif 'change_password' in request.POST:
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                return redirect(self.success_url)
            else:
                context = {
                    'user_form': UserUpdateForm(instance=request.user),
                    'avatar_form': AvatarUpdateForm(instance=avatar),
                    'password_form': password_form,
                }
                return render(request, self.template_name, context)
        
        return redirect(self.success_url)
