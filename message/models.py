from django.db import models
from django.utils import timezone
from accounts.models import MyUser


class Message(models.Model):

    date = models.DateTimeField(default=timezone.now)
    message = models.TextField()
    author = models.ForeignKey(
        MyUser, related_name='%(class)s_author', null=True,
        blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.message

