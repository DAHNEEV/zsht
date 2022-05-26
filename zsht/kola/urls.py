from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.kola, name="kola"),
    path('informatyka/', views.informatyka, name="informatyka"),
    path('matematyka/', views.matematyka, name="matematyka"),
]
