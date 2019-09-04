from django.shortcuts import render
from django.views.generic import View
from . import forms
# Create your views here.

#class candidate_create(View):
#    def get(self,request):
#        candidate_widgets = tests_form()    
#        context = {'form':candidate_widgets}
#        return render(request,'contest.html',context)
#    def post(self,request):
#        pass
def candidate_create(request):
    if request.method == 'POST':
        candidate_widgets = forms.tests_form(request.POST)
        if candidate_widgets.is_valid():
            candidate_widgets.save()
    context = {'form':forms.tests_form()}
    return render(request,'contest.html',context)


def testing_page(request): 
    context = {}
    return render(request,'test_page.html',context)
