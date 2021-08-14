from django.db import models

# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField(default=0)
    pages = models.IntegerField(default=0)
    timeStamp = models.DateField(auto_now_add=True)
    publish = models.BooleanField(default=True)
