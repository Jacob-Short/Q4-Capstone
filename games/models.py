from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from accounts.models import MyUser

# from reviews.models import Review


class Game(models.Model):
    POOR = 'poor'
    GOOD = 'good'
    GREAT = 'great'
    EXCEPTIONAL = 'exceptional'

    XBOX = 'xbox'
    PLAYSTATION = 'playstation'
    PC = 'pc'
    SWITCH = 'switch'

    SYS_CHOICES = [
        (XBOX, 'xbox'),
        (PLAYSTATION, 'playstation'),
        (PC, 'pc'),
        (SWITCH, 'switch'),
    ]

    RATING_CHOICES = [
        (POOR, 'poor'),
        (GOOD, 'good'),
        (GREAT, 'great'),
        (EXCEPTIONAL, 'exceptional'),
    ]

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=150)
    rating = models.CharField(max_length=150, choices=RATING_CHOICES)
    platform = models.CharField(max_length=150, choices=SYS_CHOICES)
    released = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    # reviews = models.ForeignKey(Review, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title