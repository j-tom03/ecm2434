from django import forms
import datetime


class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=200)
    email = forms.EmailField(label='Email', max_length=200)
    profile_image = forms.ImageField(label='Profile Image')
    password = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput)

class SetChallengeForm(forms.Form):
    challenge = forms.CharField(label='Challenge', max_length=200)


#This is probably not correct right now, I plan on sorting it but I need to figure it out first, would appreciate help understanding django
class ChallengeCompleteForm(forms.Form):
    date = datetime.datetime.today() #Idk if this is the right way to do this
    user = "" #Not sure how to do this
    photo_evidence = forms.ImageField(label="Photo Evidence", allow_empty_file=False, required=True, widget=forms.FileInput) #I think this one works?
