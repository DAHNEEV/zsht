from django.urls import path
from filedownload import views

urlpatterns = [
    path('', views.download_file),
]