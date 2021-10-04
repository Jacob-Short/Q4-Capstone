from django import forms
from django.forms.fields import EmailField


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = EmailField()


class PostForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea)