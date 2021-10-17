from django.db import models
from django.db.models.fields import DateField
from django.utils import timezone
from accounts.models import MyUser
from games.models import Game


class Review(models.Model):
    CHOICES_RATING = [
      (1, '1'),
      (2, '2'),
      (3, '3'),
      (4, '4'),
      (5, '5'),
    ]
    rating = models.CharField(choices=CHOICES_RATING, max_length=150)
    name = models.CharField(max_length=150)
    text = models.TextField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True)
    user_created = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='created_by')
    time_created = DateField(default=timezone.now)
    

    def __str__(self):
        return self.name
