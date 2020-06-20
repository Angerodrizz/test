from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image

# Create your models here.

class games(models.Model): #Category
    name=models.CharField(max_length=64)
    image = models.ImageField(verbose_name="Imagen", upload_to="games")

    def __str__(self):
        return f"{self.name}"





