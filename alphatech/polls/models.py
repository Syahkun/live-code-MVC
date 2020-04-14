from django.db import models

# Create your models here.
class Mentee(models.Model):
    image_mentee= models.CharField(max_length=100)
    nama_mentee = models.CharField(max_length=100)
    pesan_mentee = models.TextField()