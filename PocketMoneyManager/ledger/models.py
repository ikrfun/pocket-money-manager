from django.db import models

class Pay(models.Model):
    name = models.CharField(max_length=10)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add = True)
    
class Incom(models.Model):
    name = models.CharField(max_length=10)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add = True)
    

    