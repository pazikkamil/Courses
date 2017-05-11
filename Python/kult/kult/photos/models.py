from django.db import models

# Create your models here.


class Photo(models.Model):
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    format = models.CharField(max_length=20)
