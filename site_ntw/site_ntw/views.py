from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    context = {}
    return render(request,'home.html',context)
    #return HttpResponse("<h1> hello </h1>")
