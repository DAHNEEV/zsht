from django.contrib import admin
from .models import Author, Category, Article

@admin.register(Author)
class authorAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class articleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "category", "created")
    list_display_links = ("id", "title")