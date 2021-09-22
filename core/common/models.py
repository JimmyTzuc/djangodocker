import uuid
from django.db import models


class Name(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre


    class Meta:
        abstract = True


class Description(models.Model):
    descripcion = models.TextField(blank=True, default="")


    class Meta:
        abstract = True


