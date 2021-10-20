from django import forms
from django.forms.widgets import Textarea
from games.models import Game
from accounts.models import MyUser

class CreateCommunityForm(forms.Form):
    members = forms.ModelMultipleChoiceField(queryset=MyUser.objects.all())
    game = forms.ModelChoiceField(queryset=Game.objects.all())



class CreateCommunityMessageForm(forms.Form):
    message=forms.CharField(widget=Textarea)