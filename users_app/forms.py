from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #creates email field

    #configure on which model it must save
    class Meta:
        model= User
        #fields
        fields=['username','email','password1','password2']
