from django.db import models

# Create your models here.
class Pay(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=False)
    
class Incom(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now=False, auto_now_add=False)