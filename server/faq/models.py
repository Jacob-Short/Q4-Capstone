from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from accounts.models import MyUser
from games.models import Game

class UserFaq(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    email = models.EmailField()
    time_created = models.DateTimeField(default=timezone.now)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    question = models.TextField()

    def __str__ (self):
        return self.question