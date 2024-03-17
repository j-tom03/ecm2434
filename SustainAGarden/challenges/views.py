from django.contrib.auth import authenticate, login, logout
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404

from . import models
from .forms import SetChallengeForm, UserForm, LoginForm, CompleteChallengeForm, CompleteTransportForm
from .stats import generate_statistics_context

from .transport import *

# Create your views here.

def index(request):
    print(generate_fact_match_context())
    context = {}
    if request.method == "POST":
        if request.POST["form_id"] == "login":
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(request, username=form.cleaned_data["username"],
                                    password=form.cleaned_data["password"])
                if user is None:
                    context["login_error"] = "Incorrect username or password"
                elif user.institution is True:
                    login(request, user)
                    return render(request, "statistics.html", generate_statistics_context())
                else:
                    login(request, user)
                    context = generate_user_context(user)
            else:
                context["login_error"] = "Incorrect username or password"

        elif request.POST["form_id"] == "register":
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                user = authenticate(request,
                                    username=form.cleaned_data["username"],
                                    password=form.cleaned_data["password1"])
                login(request, user)
                context = generate_user_context(user)

        elif request.POST["form_id"] == "complete_challenge":
            form = CompleteChallengeForm(request.POST)
            if form.is_valid():
                models.Challenge(challenge_ID=request.POST["challenge_ID"],
                                 user=request.user).save()
                request.user.coins += models.Challenge.objects.get(challenge_ID=request.POST["challenge_ID"]).coins
                request.user.completed_challenges += ","+request.POST["challenge_ID"]
                request.user.save()

        elif request.POST["form_id"] == "transport_challenge":
            form = CompleteTransportForm(request.POST)
            if form.is_valid():
                if not validate_format(form.cleaned_data["start_point"]) or not validate_format(form.cleaned_data["end_point"]):
                    context["format_error"] = """Start point or end point do not fit the required format,
                                                 Correct format: *word*.*word*.*word*"""

                else:
                    distance = get_distance(form.cleaned_data["start_point"], form.cleaned_data["end_point"])
                    if isinstance(distance, tuple):
                        context["distance_error"] = f"An error occurred: {distance[1]}\nError code: {distance[0]}"
                    else:
                        models.CompleteChallenge(challenge_ID=request.POST["challenge_ID"],
                                                 user=request.user).save()
                        tran_chall = models.transport_challenge.objects.get(challenge_ID=request.POST["challenge_ID"])
                        tran_chall.distance_covered = distance
                        tran_chall.start_point = form.cleaned_data["start_point"]
                        tran_chall.end_point = form.cleaned_data["end_point"]
                        tran_chall.save()
                        context["distance"] = distance
                        request.user.coins += round(distance*30)
                        request.user.completed_challenges += request.POST["challenge_ID"]
                        request.user.save()

        elif request.POST["form_id"] == "logout":
            logout(request)

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

    # new context for statistics page
    """
    context = generate_statistics_context()
    """
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
    context = {"username": user.username, "challenges_completed": len(user.completed_challenges.split(",")),
               "coins": user.coins, "garden": user.garden,
               "challenges": models.Challenge.objects.filter(challenge_setter=user),
               "profile_image": user.profile_image, "setter": user.setter}
    return context


def populate_user_model(data):
    user = models.User(username=data["username"], email=data["email"], profile_image=data["profile_image"],
                       password=data["password"])
    user.save()

def generate_fact_match_context():
    fact_model = models.FactMatchModel.objects.all()
    # have this return a different fact each day
    first = fact_model[0]
    full = first.text
    split_full = full.split(" ")
    words = first.words.split(",")
    word_list = []
    for word in words:
        word_list.append(split_full[int(word)])
        split_full[int(word)] = "______"

    fact = " ".join(split_full)

    context = {"fact": fact, "word_list": word_list}
    return context
