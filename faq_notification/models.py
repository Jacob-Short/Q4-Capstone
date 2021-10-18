from django.db import models
from accounts.models import MyUser
from django.db.models.deletion import CASCADE
from faq.models import UserFaq

class FaqNotification(models.Model):
    CHOICES = [(1, 'True'), (2, 'False')]
    faq = models.ForeignKey(UserFaq, on_delete=CASCADE, null=True, related_name='faq_noti')
    user_notified = models.ForeignKey(MyUser, on_delete=CASCADE, null=True, related_name='user_notified_faq')
    isNew = models.BooleanField(choices=CHOICES, default=1)