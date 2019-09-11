from django.shortcuts import render
from review.forms import reviewForm,programForm,logInForm,createAccountForm
from review.models import candidates
# Create your views here.
def create(request):
    if request.method == 'POST':
        saveForm = reviewForm(request.POST,request.FILES)
        if saveForm.is_valid():
            saveForm.save() 
    reviewerForm = reviewForm()
    progForm = programForm()
    context = {'form':reviewerForm,'ProgForm':progForm}
    return render(request,'contest.html',context)
def show(request):
    ctx = {'candidates':candidates.objects.all()}
    return render(request,'admin_reviews.html',ctx)
    
def auth_view(request):

    loginForm   = logInForm()
    signupForm  = createAccountForm()
    ctx = {
            'logInForm':loginForm,
            'signUpForm':signupForm,
            }
    return render(request,'candidatesAuth.html',ctx)
def LogIn_view(request):
    if request.method == "POST":
        a = 0
    
    loginForm = logInForm()
    ctx = {
            'logInForm':loginForm,
            }
    return render(request,'candidateslogIn.html',ctx)


def SignUp_view(request):
    if request.method == "POST":
        a = 0

    SignupForm = createAccountForm()
    ctx = {
            'signUpForm':SignupForm, 
            }
    return render(request,'candidatesSignUP.html',ctx)




