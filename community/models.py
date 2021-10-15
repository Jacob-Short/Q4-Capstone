from django.db import models
from django.utils import timezone

from accounts.models import MyUser
from games.models import Game
from review.models import Review
from faq.models import UserFaq
from message.models import Message

class Community(models.Model):
    '''a sub community become available to group of 2 or more, when they
    have left a review for the same game'''
    creator = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    members = models.ManyToManyField(MyUser, related_name='comm_members')
    messages = models.ManyToManyField(Message, related_name='comm_messages')
    time_created = models.DateTimeField(default=timezone.now)