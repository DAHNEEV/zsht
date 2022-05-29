from pyexpat import model
from django.db import models
from django.forms import forms
from tinymce import models as tinymce_models

class Author(models.Model):
    author = models.CharField(max_length=64, verbose_name="Autor")

    def __str__(self):
        return str(self.author)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autorzy'

class Upload(models.Model):
    title = models.CharField(max_length=128, verbose_name="Tytuł")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, verbose_name="Autor")
    created = models.DateField(null=True, verbose_name="Utworzone")
    file = models.FileField()

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Artykuł'
        verbose_name_plural = 'Artykuły'