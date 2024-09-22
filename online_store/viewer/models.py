from django.db import models
from django.contrib.auth.models import User


class Potraviny(models.Model):
    potravina = models.CharField(max_length=100)
    cena = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.potravina} - {self.cena}"