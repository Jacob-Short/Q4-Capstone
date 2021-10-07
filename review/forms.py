from django import forms
from games.models import Game


class CreateReviewForm(forms.Form):
    name = forms.CharField(max_length=150)
    text = forms.CharField(widget=forms.Textarea)
    game = forms.ModelChoiceField(queryset=Game.objects.all())