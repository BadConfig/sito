from django.shortcuts import render

def auth_view(request):
    ctx = {}
    return render(request,'auth.html',ctx)
