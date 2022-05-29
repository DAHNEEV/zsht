from django.shortcuts import render
from .models import Upload

def kola(request):
    uploads = { 'uploads': Upload.objects.all().order_by('-id') }
    return render(request, 'kola/main.html', uploads)

def profile(request):
    return render(request, 'kola/profile.html')