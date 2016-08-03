from django.shortcuts import render

# Create your views here.

def temp(request):
    render(request,'index.html',{})