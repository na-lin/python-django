from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("This works")


def feburary(request):
    return HttpResponse("Work for at least 20 minutes every day!")
