
from django.db import models
from django.contrib.auth.models import AbstractUser
# from games.models import Game

# Create your models here.
class MyUser(AbstractUser):
    gamer_tag = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField()
    picture = models.ImageField(upload_to='images/', max_length=100, default='images/download.png')
    bio = models.TextField(null=True, blank=True)
    # favorite_game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.username