from django.shortcuts import render

def kola(request):
    return render(request, 'home/home.html')
