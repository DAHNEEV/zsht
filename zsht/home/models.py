from pyexpat import model
from django.db import models
from django.forms import forms

class Author(models.Model):
    author = models.CharField(max_length=64)

    def __str__(self):
        return str(self.author)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autorzy'

class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return str(self.category)

    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'

class Article(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Artykuł'
        verbose_name_plural = 'Artykuły'