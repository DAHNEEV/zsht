from django.contrib import admin
from .models import Author, Category, Article

@admin.register(Author)
class authorAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["author"].label = "Autor"
        return form

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["category"].label = "Kategoria"
        return form

@admin.register(Article)
class articleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category")

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["title"].label = "Tytuł"
        form.base_fields["description"].label = "Opis"
        form.base_fields["author"].label = "Autorzy"
        form.base_fields["category"].label = "Kategoria"
        return form