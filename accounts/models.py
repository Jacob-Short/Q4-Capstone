from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    homepage = models.URLField(null=True, blank=True)
    displayname = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField()
    picture = models.ImageField(upload_to=None, max_length=100)

    def __str__(self):
        return self.username