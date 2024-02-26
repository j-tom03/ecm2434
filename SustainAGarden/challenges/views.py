from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from . import models
from .forms import SetChallengeForm, UserForm, LoginForm, CompleteChallengeForm

# Create your views here.

def index(request):
    context = {}
    if request.method == "POST":
        if request.POST["form_id"] == "login":
            form = LoginForm(request.POST)
            if form.is_valid():
                context = generate_user_context(form.cleaned_data["username"])


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


def setChallenge(request):
    if request.method == "POST":
        form = SetChallengeForm(request.POST)
        if form.is_valid():
            return HttpResponse("thanks for the challenge!")

    else:
        form = SetChallengeForm()

    return render(request, "name.html", {"form": form})

def generate_user_context(username):
    context = {"username": username}
    context["challenges_completed"] = len(models.User.objects.get(username=username).completed_challenges)
    context["coins"] = models.User.objects.get(username=username).coins
    context["garden"] = models.User.objects.get(username=username).garden
    context["challenges"] = models.Challenge.objects.all()
    context["profile_image"] = models.User.objects.get(username=username).profile_image
    return context

def populate_user_model(data):
    user = models.User(username=data["username"], email=data["email"], profile_image=data["profile_image"], password=data["password"])
    user.save()
