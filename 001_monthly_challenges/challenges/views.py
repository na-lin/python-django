from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def january(request):
    return HttpResponse("Eat no meat for the entire month!")


def feburary(request):
    return HttpResponse("Work for at least 20 minutes every day!")
