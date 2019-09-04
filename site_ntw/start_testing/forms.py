from django import forms

class tests_form(forms.Form):
    first_name      = forms.CharField(max_length=20)
    last_name       = forms.CharField(max_length=20)
    email           = forms.EmailField()
    telegram_contact= forms.CharField(max_length=20)
    about_candidate = forms.CharField(max_length=80)
    solved_quizez   = forms.FileField()
    
    def save(self):
        new_candidate = candidates_data.objects.create(
                first_name      = self.cleaned_data['first_name'],
                last_name       = self.cleaned_data['last_name'],
                email           = self.cleaned_data['email'],
                telegram_contact= self.cleaned_data['telegram_contact'],
                about_candidate = self.cleaned_data['about_candidate'],
                solved_quizez   = self.cleaned_data['solved_quizez'],
                )
        return new_candidate

