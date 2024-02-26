from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=200)
    email = forms.EmailField(label='Email', max_length=200)
    profile_image = forms.ImageField(label='Profile Image')
    setter = forms.BooleanField(label='Setter', required=False)
    institution = forms.BooleanField(label='Institution', required=False)
    password = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=200)
    password = forms.CharField(label="Password", max_length=200, widget=forms.PasswordInput)


class SetChallengeForm(forms.Form):
    challenge = forms.CharField(label='Challenge', max_length=200)

class CompleteChallengeForm(forms.Form):
    pass