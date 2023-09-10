from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


def monthly_challenges(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no meat for the entire month!"
    elif month == "feburary":
        challenge_text = "Work for at least 20 minutes every day!"
    elif month == "march":
        challenge_text = "Learn Django at least 20 minutes every day!"
    else:
        return HttpResponseNotFound("This month is not supported.")
    return HttpResponse(challenge_text)
