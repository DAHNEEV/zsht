from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.kola, name="kola-main"),
    path('login/', auth_views.LoginView.as_view(template_name='kola/login.html'), name="kola-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='kola/logout.html'), name="kola-logout"),
    path('profile/', views.profile, name='kola-profile'),
]
