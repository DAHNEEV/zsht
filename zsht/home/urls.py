from django.contrib import admin
from django.urls import path
from . import views
from .views import ArticleDetailView

urlpatterns = [
    path('', views.home, name="zsht-home"),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="zsht-article"),
]
