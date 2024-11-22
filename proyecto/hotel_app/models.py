from django.db import models
# Create your models here.
class hotel(models.Model):
    id_habitaciones=models.CharField(max_length=6)