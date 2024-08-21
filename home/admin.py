from django.contrib import admin
# from .models import Student
from home.models import Student

# Register your models here.
# admin.site.register(Student)

@admin.register(Student)
class StudentAdminPanel(admin.ModelAdmin):
    list_display = ['name', 'address','phone']
    search_fields = ['name']
    # readonly_fields = ['name']