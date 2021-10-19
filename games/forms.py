from django import forms
from games.models import Game


class CreateGameForm(forms.Form):
    POOR = 'poor'
    GOOD = 'good'
    GREAT = 'great'
    EXCEPTIONAL = 'exceptional'

    XBOX = 'xbox'
    PLAYSTATION = 'playstation'
    PC = 'pc'
    SWITCH = 'switch'

    SYS_CHOICES = [
        (XBOX, 'xbox'),
        (PLAYSTATION, 'playstation'),
        (PC, 'pc'),
        (SWITCH, 'switch'),
    ]

    RATING_CHOICES = [
        (POOR, 'poor'),
        (GOOD, 'good'),
        (GREAT, 'great'),
        (EXCEPTIONAL, 'exceptional'),
    ]

    name = forms.CharField(max_length=150)
    slug = forms.CharField(max_length=150)
    rating = forms.ChoiceField(choices=RATING_CHOICES)
    platform = forms.ChoiceField(choices=SYS_CHOICES)
    released_at = forms.DateField()
    image_background = forms.ImageField()