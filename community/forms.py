from django import forms
from games.models import Game
from accounts.models import MyUser

class CreateCommunityForm(forms.Form):
    members = forms.ModelMultipleChoiceField(MyUser)