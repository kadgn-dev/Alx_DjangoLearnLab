from django.contrib import admin
from .models import Book

# Basic registration
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')   # columns visible in admin list view
    search_fields = ('title', 'author')                      # search bar for title or author
    list_filter = ('publication_year',)                      # sidebar filter for publication year
