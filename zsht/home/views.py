from django.shortcuts import render
from .models import Article
from django.views.generic.detail import DetailView

def home(request):
    articles = { 'articles': Article.objects.all() }
    return render(request, 'home/home.html', articles)

class ArticleDetailView(DetailView):
    model = Article