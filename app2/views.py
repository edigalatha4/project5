from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def latha(request):
    return HttpResponse('<b>latha is very short girl</b>')

def joshi(request):
    return HttpResponse('<b><i>joshi is very cute girl</i></b>')
