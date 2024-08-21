from django.contrib import admin
from book.models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'price', 'Created_at', 'Modified_at']