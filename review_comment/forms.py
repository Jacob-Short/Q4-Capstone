from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS
from django.db.models import query
from review_comment.models import ReviewComment
from django import forms
from mptt.forms import TreeNodeChoiceField

class AddInitialReviewCommentForm(forms.Form):
    comment = forms.CharField(max_length=300,)

class AddReviewCommentForm(forms.Form):
    comment = forms.CharField(max_length=300)
    parent = TreeNodeChoiceField(queryset=ReviewComment.objects.all(), level_indicator="+--", required=False)