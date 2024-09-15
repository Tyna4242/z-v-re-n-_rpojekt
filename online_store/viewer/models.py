from django.db import models
from django.contrib.auth.models import User


class Potraviny(models.Model):
    pecivo = models.CharField(max_length=100)
    ovoce = models.CharField(max_length=100)
