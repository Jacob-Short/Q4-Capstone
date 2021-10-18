from django.db import models
from accounts.models import MyUser
from django.db.models.deletion import CASCADE
from review.models import Review

class Notification(models.Model):
    CHOICES = [(1, 'True'), (2, 'False')]
    review = models.ForeignKey(Review, on_delete=CASCADE, null=True, related_name='review_noti')
    user_notified = models.ForeignKey(MyUser, on_delete=CASCADE, null=True, related_name='user_notified_review')
    isNew = models.BooleanField(choices=CHOICES, default=1)