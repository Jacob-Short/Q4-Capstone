from django import forms
from games.models import Game


class CreateReviewForm(forms.Form):
    LOW=1
    MODERATE=2
    OK=3 
    GOOD=4 
    AWESOME=5
    CHOICES_RATING = [
      (LOW,'low'),
      (MODERATE,'moderate'),
      (OK,'ok'),
      (GOOD,'good'),
      (AWESOME,'awesome'),
    ]
    rating = forms.ChoiceField(choices=CHOICES_RATING)
    name = forms.CharField(max_length=150)
    text = forms.CharField(widget=forms.Textarea)
  
    