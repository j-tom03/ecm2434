from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserForm(UserCreationForm):

    """username = forms.CharField(label='Username', max_length=200)
    email = forms.EmailField(label='Email', max_length=200)
    profile_image = forms.ImageField(label='Profile Image')
    setter = forms.BooleanField(label='Setter', required=False)
    institution = forms.BooleanField(label='Institution', required=False)
    password = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput)"""

    image = forms.ChoiceField(label='Profile Image', choices=[('dog', 'dog'), ('man', 'man'), ('shark', 'shark'), ('obamna', 'obama')])

    class Meta:
        model = User
        fields = ['username', 'email', 'image', 'setter', 'institution', 'password1', 'password2']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'image', 'setter', 'institution', 'password']

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=200)
    password = forms.CharField(label="Password", max_length=200, widget=forms.PasswordInput)


class SetChallengeForm(forms.Form):
    title = forms.CharField(label='Challenge', max_length=200)
    coins = forms.IntegerField(label='Coins')
    description = forms.CharField(label='Description', widget=forms.Textarea)


class CompleteChallengeForm(forms.Form):
    evidence = forms.ImageField(label="Input evidence here")


class CompleteTransportForm(forms.Form):
    start_point = forms.CharField(label="start point")
    end_point = forms.CharField(label="end point")


