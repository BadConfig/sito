from django import forms
from review.models import candidates

class reviewForm(forms.Form):
    firstName = forms.CharField(label ='Your name')
    lastName = forms.CharField(label ='Your last name')
    email = forms.EmailField()
    about = forms.SlugField(label ='tell smth about you')
    def save(self):
        modelForm = candidates(
                firstName = self.cleaned_data['firstName'],
                lastName = self.cleaned_data['lastName'],
                email = self.cleaned_data['email'],
                about = self.cleaned_data['about'],
                )
        modelForm.save()
        return modelForm
