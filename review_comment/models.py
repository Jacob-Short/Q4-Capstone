from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from mptt.models import MPTTModel, TreeForeignKey
from accounts.models import MyUser
from review.models import Review

class ReviewComment(MPTTModel):
    comment = models.CharField(max_length=300)
    review = models.ForeignKey(Review, on_delete=CASCADE, related_name="parent_review")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    user_created = models.ForeignKey(MyUser, on_delete=CASCADE, null=True, related_name='user_created')

    def __str__(self):
        return self.comment


    class MPTTMeta:
        order_insertion_by = ['comment']

