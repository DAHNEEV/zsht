from django.contrib import admin
from django.urls import path
from . import views
from .views import ArticleDetailView
from .views import ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(), name="zsht-home"),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="zsht-article"),
]
