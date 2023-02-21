from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    '''
    Form used when a user registers an account, uses inbuilt django UserCreationForm
    '''
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
    
    def __init__(self, *args, **kwargs):
        '''
        Removes some of the help text for logging in django automatically uses
        '''
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None