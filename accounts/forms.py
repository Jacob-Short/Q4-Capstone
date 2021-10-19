from django import forms
from django.db.models.fields import TextField
from django.forms.fields import EmailField

from games.models import Game

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = EmailField()
    gamer_tag = forms.CharField(max_length=30)


class EditProfileForm(forms.Form):
    email = forms.EmailField()
    picture = forms.ImageField(required=False)
    bio = forms.CharField(widget=forms.Textarea)
    gamer_tag = forms.CharField(max_length=30)
    favorite_game = forms.ModelChoiceField(queryset=Game.objects.all())


class SearchUserForm(forms.Form):
    gamer_tag = forms.CharField(max_length=150)