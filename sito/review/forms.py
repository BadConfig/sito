from django import forms
from review.models import candidates
from django.db import models


class reviewForm(forms.ModelForm):
    class Meta:
        model = candidates
        fields = ['firstName','lastName','email','about','program']
