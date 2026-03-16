from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inex(request):
    return HttpResponse("Hello, world!")