from faq_comment.models import FaqComment
from django import forms
from mptt.forms import TreeNodeChoiceField




class AddInitialFaqCommentForm(forms.Form):
    comment = forms.CharField(max_length=200)



class AddFaqCommentForm(forms.Form):
    answer = forms.CharField(max_length=200)