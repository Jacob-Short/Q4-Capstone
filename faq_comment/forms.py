from faq_comment.models import FaqComment
from django import forms
from mptt.forms import TreeNodeChoiceField

from faq.models import UserFaq


class AddFaqCommentForm(forms.Form):
    comment = forms.CharField(max_length=200)
    parent = TreeNodeChoiceField(queryset=UserFaq.objects.all(), level_indicator="+--")