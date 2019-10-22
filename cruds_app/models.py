from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField(unique=True, blank=True, )
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    c_name = models.CharField(max_length=32)
    email = models.EmailField(unique=True )
    phone_no = models.IntegerField()
    company = models.CharField(max_length=32)
    message = models.TextField()

    def __str__(self):
        return self.c_name