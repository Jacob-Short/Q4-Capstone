from django.db import models
from django.db.models.enums import TextChoices
from django.utils import timezone
from accounts.models import MyUser


class Message(models.Model):

    date = models.DateTimeField(default=timezone.now)
    message = models.TextField(max_length=500)
    author = models.ForeignKey(
        MyUser, related_name='%(class)s_author', null=True,on_delete=models.CASCADE)
    recipient = models.ForeignKey(
        MyUser, related_name='%(class)s_recipient', null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.message

