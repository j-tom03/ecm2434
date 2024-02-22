from django import forms
from .models import Fact

class NewFactForm(forms.ModelForm):
    fact = forms.CharField(label='Fact', max_length=200)
    class Meta:
        model = Fact
        fields = ['fact']   