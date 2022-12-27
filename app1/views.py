from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1>this is first program in app1')

def second(request):
    return HttpResponse('<h1>this is second view in app1</h1>')
