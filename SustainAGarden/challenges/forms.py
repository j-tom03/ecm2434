from django import forms


class userForm(forms.Form):
    username = forms.CharField(label='Username', max_length=200)
    email = forms.EmailField(label='Email', max_length=200)
    password = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput)

class setChallengeForm(forms.Form):
    challenge = forms.CharField(label='Challenge', max_length=200)