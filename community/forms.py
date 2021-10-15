from django import forms
from games.models import Game
from accounts.models import MyUser

class FaqForm(forms.Form):
    members = forms.ModelMultipleChoiceField(MyUser)