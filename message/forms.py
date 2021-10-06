from django import forms
from .models import Message

class AddTextForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']