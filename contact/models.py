from django.db import models

# Create your models here.

class Contact(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()