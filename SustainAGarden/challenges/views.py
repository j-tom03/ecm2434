from django.contrib.auth import authenticate, login, logout
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
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
                login(request, user)
                context = generate_user_context(user)
            else:
                context["login_error"] = "Incorrect username or password"

        elif request.POST["form_id"] == "register":
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                user = authenticate(request, username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
                login(request, user)
                context = generate_user_context(user)

        elif request.POST["form_id"] == "complete_challenge":
            form = CompleteChallengeForm(request.POST)

        elif request.POST["form_id"] == "logout":
            logout(request)
            context["login_form"] = LoginForm()
            context["register_form"] = UserForm()
            context["complete_challenge_form"] = CompleteChallengeForm()
            return render(request, "index.html", context)

    else:
        if request.user.is_authenticated:
            context = generate_user_context(request.user)

        context["login_form"] = LoginForm()
        context["register_form"] = UserForm()
        context["complete_challenge_form"] = CompleteChallengeForm()

    return render(request, "index.html", context)


def statistics(request):
    challenges = 0
    for user in models.User.objects.all():
        challenges += len(user.completed_challenges.split(","))
    context = {
        "users": models.User.objects.all(),
        "completed_challenges": challenges,
        "co2": (challenges * models.User.objects.all().count()) + 100,

    }
    return render(request, "statistics.html", context=context)

def set_challenge(request):
    if request.method == "POST":
        form = SetChallengeForm(request.POST)
        if form.is_valid():
            challenge = models.Challenge(title=form.cleaned_data['title'], transport=form.cleaned_data["transport"],
                                         coins=form.cleaned_data['coins'], description=form.cleaned_data['description'],
                                         challenge_setter=request.user)
            try:
                challenge.save()
            except Exception as e:
                print(f"An error occurred: {e}")
            return render(request, "setChallenge.html", {"form": form})
        else:
            print("POST request")
            print(form.errors)
    else:
        print("GET request")
        form = SetChallengeForm()

    return render(request, "setChallenge.html", {"form": form})

def all_challenges(request):
    challenges = models.Challenge.objects.all()
    for challenge in challenges:
        print(challenge.title)
    return render(request, "allChallenges.html", {"challenges": challenges})

def generate_user_context(user):
    context = {"username": user.username}
    context["challenges_completed"] = len(user.completed_challenges.split(","))
    context["coins"] = user.coins
    context["garden"] = user.garden
    context["challenges"] = models.Challenge.objects.filter(challenge_setter=user)
    context["profile_image"] = user.profile_image
    context["setter"] = user.setter
    return context

def populate_user_model(data):
    user = models.User(username=data["username"], email=data["email"], profile_image=data["profile_image"],
                       password=data["password"])
    user.save()
