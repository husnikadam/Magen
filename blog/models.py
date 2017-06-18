from django.db import models
from django.utils import timezone


class Product(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    price = models.CharField(max_length=20)

    
    def __str__(self):
        return self.title
