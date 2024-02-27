from django.contrib.auth import authenticate
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from . import models
from .forms import SetChallengeForm, UserForm, LoginForm, CompleteChallengeForm
from .stats import generate_statistics_context

import hashlib

# Create your views here.

def index(request):
    context = {}
    if request.method == "POST":
        if request.POST["form_id"] == "login":
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(request, username=form.cleaned_data["username"], password=form.cleaned_data["password"])
                if user is None:
                    context["login_form"] = LoginForm()
                    context["register_form"] = UserForm()
                    context["complete_challenge_form"] = CompleteChallengeForm()
                    context["login_error"] = "Incorrect username or password"
                    return render(request, "index.html", context)
                if user.institution:
                    return render(request, "statistics.html", generate_statistics_context())
                context = generate_user_context(user)
            else:
                context["login_error"] = "Incorrect username or password"

        elif request.POST["form_id"] == "register":
            form = UserForm(request.POST)
            if form.is_valid():
                context = generate_user_context(form.cleaned_data["username"])
                populate_user_model(context)

        elif request.POST["form_id"] == "complete_challenge":
            form = CompleteChallengeForm(request.POST)

    else:
        context["login_form"] = LoginForm()
        context["register_form"] = UserForm()
        context["complete_challenge_form"] = CompleteChallengeForm()

    return render(request, "index.html", context)

def statistics(request):
    return render(request, "statistics.html")

def setChallenge(request):
    if request.method == "POST":
        form = SetChallengeForm(request.POST)
        if form.is_valid():
            return HttpResponse("thanks for the challenge!")

    else:
        form = SetChallengeForm()

    return render(request, "name.html", {"form": form})

def generate_user_context(user):
    context = {"username": user.username}
    context["challenges_completed"] = len(user.completed_challenges.split(","))
    context["coins"] = user.coins
    context["garden"] = user.garden
    context["challenges"] = models.Challenge.objects.filter(challenge_setter=user)
    context["profile_image"] = user.profile_image
    return context

def populate_user_model(data):
    user = models.User(username=data["username"], email=data["email"], profile_image=data["profile_image"],
                       password=data["password"])
    user.save()
