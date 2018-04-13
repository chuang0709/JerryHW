from django.shortcuts import render
from django.http import HttpResponse


def index(request):
     return HttpResponse("Hello mom I'm Here")
# Create your views here.
