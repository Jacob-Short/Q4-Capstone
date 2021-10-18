from django import forms
from .models import Message

class AddTextForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))