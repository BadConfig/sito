from django.shortcuts import render
from review.forms import reviewForm
from review.models import candidates
# Create your views here.
def create(request):
    if request.method == 'POST':
        saveForm = reviewForm(request.POST,request.FILES)
        if saveForm.is_valid():
            saveForm.save() 
    reviewerForm = reviewForm()
    context = {'form':reviewerForm}
    return render(request,'contest.html',context)
def show(request):
    ctx = {'candidates':candidates.objects.all()}
    return render(request,'admin_reviews.html',ctx)
    
