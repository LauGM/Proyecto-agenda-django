from django import forms
from django.contrib.auth.models import User
from .models import Avatar
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

class RegisterForm(UserCreationForm):    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class AvatarUpdateForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        # Aquí puedes personalizar los labels o widgets si lo necesitas
        pass