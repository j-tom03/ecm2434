from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from . import setChallengeForm

# Create your views here.

def index(request):
    context = {}
    return render(request, "index.html", context)


def login(request):
    pass


def register(request):
    pass


def challenge(request, challenge_id):
    return HttpResponse("You're looking at challenge %s." % challenge_id)


def setChallenge(request):
    if request.method == "POST":
        form = setChallengeForm(request.POST)
        if form.is_valid():
            return HttpResponse("thanks for the challenge!")

    else:
        form = setChallengeForm()

    return render(request, "name.html", {"form": form})
