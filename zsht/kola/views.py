from django.shortcuts import render
from .models import Upload
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def kola(request):
    uploads = { 'uploads': Upload.objects.all().order_by('-id') }
    return render(request, 'kola/main.html', uploads)

@login_required
def profile(request):
    return render(request, 'kola/profile.html')