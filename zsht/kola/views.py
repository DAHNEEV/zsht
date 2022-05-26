from django.shortcuts import render

def kola(request):
    return render(request, 'home/home.html')

def informatyka(request):
    return render(request, 'home/home.html')

def matematyka(request):
    return render(request, 'home/home.html')

