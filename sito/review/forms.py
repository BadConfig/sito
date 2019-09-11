from django import forms
from review.models import candidates,program,userAccount
from django.db import models

class createAccountForm(forms.ModelForm):
    class Meta:
        model = userAccount
        fields = ['email','password']

class logInForm(forms.ModelForm):
    class Meta:
        model = userAccount
        fields = ['email','password','password']

class reviewForm(forms.ModelForm):
    class Meta:
        model = candidates
        fields = ['firstName','lastName','email','about','program']
class programForm(forms.ModelForm):
    class Meta:
        model = program
        REQFIELDS = [
                'typeOfLang',
                'typeOfProg',
                'progInFile',
                'progInText',
                ]
        fields = REQFIELDS
