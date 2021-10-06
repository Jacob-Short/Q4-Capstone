from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import AbstractUser
# from games.models import Game

# Create your models here.
class MyUser(AbstractUser):
    displayname = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField()
    picture = models.ImageField(upload_to=None, max_length=100)
    bio = models.TextField()
    # favorite_game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.username