from django.shortcuts import render
from django.http import HttpResponse

from .models import Fact
from .forms import NewFactForm

# Create your views here.
def give_fact(request):
    return HttpResponse("This is a fact")

def add_fact(request):
    if request.method == "POST":
        form = NewFactForm(request.POST)
        if form.is_valid():
            return HttpResponse("thanks for the fact!")

    else:
        form = NewFactForm()

    return render(request, "name.html", {"form": form})