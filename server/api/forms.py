from django import forms


class SearchApiForm(forms.Form):
    search = forms.CharField(max_length=100)