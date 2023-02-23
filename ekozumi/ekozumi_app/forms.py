from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class ZumiCreationForm(forms.Form):
    petName = forms.CharField(label="Zumi name", max_length=50)
    petType = forms.CharField(max_length=9, label='Zumi type', widget=forms.RadioSelect(choices=PET_CHOICES), initial='HEDGEHOG'  )
    
    class Meta:
        model = Pet
        fields = ('petName', 'petType')
