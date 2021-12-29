from django import forms
from django.db.models.fields import TextField
from django.forms.fields import EmailField

from games.models import Game
from accounts.models import MyUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = EmailField()
    gamer_tag = forms.CharField(max_length=30)

    def clean(self):
        super(SignupForm, self).clean()

        # list of possible domains
        domain_list = [".com", ".edu", ".org", ".net", ".gov", ".biz"]

        # get fields from form
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")
        gamer_tag = self.cleaned_data.get("gamer_tag")

        """
        can use raise ValidationError - although then we 
            cannot set the _errors title with desc

        from django.core.exceptions import ValidationError
        raise ValidationError(
          "Please use a valid domain."
        )
        """

        # domain validation
        if email[-4:] not in domain_list:
            self._errors["email-domail"] = self.error_class(
                ["Please use a valid domain."]
            )

        # IntegreityError: [ UNIQUE contraint failed (username) ]
        existing_usernames = [member.username for member in MyUser.objects.all()]
        if username in existing_usernames:
            self._errors["existing-username"] = self.error_class(
                ["Username has been taken, please try a new one."]
            )

        # IntegreityError: [ UNIQUE contraint failed (gamer_tag) ]
        existing_gamer_tags = [user.gamer_tag for user in MyUser.objects.all()]
        if gamer_tag in existing_gamer_tags:
            self._errors["existing-gamer_tag"] = self.error_class(
                ["Gamer Tag has been taken, please try a new one."]
            )

        # TODO:
        # possiblity of giving a few suggestions based off 1st attempt
        # ex: input = dave, possibilities = ['dave0, 'dave1', 'davey']

        # possible validation for password

        return self.cleaned_data


class EditProfileForm(forms.Form):
    email = forms.EmailField()
    picture = forms.ImageField(required=False)
    bio = forms.CharField(widget=forms.Textarea)
    gamer_tag = forms.CharField(max_length=30)
    favorite_game = forms.ModelChoiceField(queryset=Game.objects.all())


class SearchUserForm(forms.Form):
    gamer_tag = forms.CharField(max_length=150)
