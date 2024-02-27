from django import forms
from .models import User


class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=200)
    email = forms.EmailField(label='Email', max_length=200)
    profile_image = forms.ImageField(label='Profile Image')
    setter = forms.BooleanField(label='Setter', required=False)
    institution = forms.BooleanField(label='Institution', required=False)
    password = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'profile_image', 'setter', 'institution', 'password']

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=200)
    password = forms.CharField(label="Password", max_length=200, widget=forms.PasswordInput)


class SetChallengeForm(forms.Form):
    challenge = forms.CharField(label='Challenge', max_length=200)


class CompleteChallengeForm(forms.Form):
    pass
