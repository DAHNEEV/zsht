from django.shortcuts import render
from .models import Article
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class ArticleListView(ListView):
    model = Article
    template_name = 'home/home.html'
    ordering = ['-id']
    paginate_by = 5

class ArticleDetailView(DetailView):
    model = Article