from django.contrib import admin
from .models import Author, Upload

@admin.register(Author)
class authorAdmin(admin.ModelAdmin):
    pass

@admin.register(Upload)
class uploadAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "created")
    list_display_links = ("id", "title")