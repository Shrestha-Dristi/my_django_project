from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True, help_text="Name of the book")
    price = models.PositiveIntegerField()
    isbn_no = models.CharField(unique=True, max_length=40)
    author = models.CharField(max_length=80, null=True, blank=True)
    published_date = models.DateField()
    Created_at = models.DateTimeField(auto_now_add=True)
    Modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name