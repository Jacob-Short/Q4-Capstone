from django import forms

class FaqForm(forms.Form):
    question = forms.CharField(widget=forms.Textarea)