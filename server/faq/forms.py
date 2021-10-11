from django import forms
from django.db.models.fields import TextField
from games.models import Game

class FaqForm(forms.Form):
    email = forms.EmailField()
    game = forms.ModelChoiceField(queryset=Game.objects.all())
    question = forms.CharField(widget=forms.Textarea)