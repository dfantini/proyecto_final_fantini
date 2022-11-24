from django import forms 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from smbapp.models import *



#Form to create instrument
class FormCreatInstrument (forms.ModelForm):
    name = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Instrument
        fields = ['name']

#Form Creat User
class FormCreateUser (UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField (label='Password', widget=forms.PasswordInput)
    password1 = forms.CharField (label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','username' , 'password1', 'password2']
        help_texts = {k:'' for k in fields}