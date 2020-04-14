from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.
class JualProduk(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.CharField(max_length=100)
    kategori_id = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name