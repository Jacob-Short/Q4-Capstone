from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from mptt.models import MPTTModel, TreeForeignKey
from accounts.models import MyUser

from faq.models import UserFaq


class FaqComment(MPTTModel):
    comment = models.CharField(max_length=200)
    faq = models.ForeignKey(UserFaq, on_delete=CASCADE, related_name="parent_faq")
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    user = models.ForeignKey(MyUser, on_delete=CASCADE, null=True, related_name='user_filed')

    def __str__(self):
        return self.comment


    class MPTTMeta:
        order_insertion_by = ['comment']
