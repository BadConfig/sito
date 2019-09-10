from django import forms
from review.models import candidates,program
from django.db import models



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
