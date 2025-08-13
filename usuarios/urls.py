from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('avatar/', views.AvatarUpdateView.as_view(), name='avatar'),
]