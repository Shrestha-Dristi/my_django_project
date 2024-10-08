from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=60, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone = models.PositiveIntegerField()
    phone1 = models.IntegerField()
    dob = models.DateField()

    def __str__(self):
        return self.name
