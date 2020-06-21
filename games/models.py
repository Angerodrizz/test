from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image

class Item(models.Model): #Category
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="images")
    link = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.title

class Console_games(models.Model): #Category
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="images")
    link = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.title


# Create your models here.
