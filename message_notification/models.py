from django.db import models
from accounts.models import MyUser
from django.db.models.deletion import CASCADE
from message.models import Message

class Notification(models.Model):
    CHOICES = [(1, 'True'), (2, 'False')]
    message = models.ForeignKey(Message, on_delete=CASCADE, null=True, related_name='message_noti')
    user_notified = models.ForeignKey(MyUser, on_delete=CASCADE, null=True, related_name='user_notified_message')
    isNew = models.BooleanField(choices=CHOICES, default=1)