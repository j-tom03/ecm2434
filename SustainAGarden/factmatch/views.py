from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def give_fact(request):
    return HttpResponse("This is a fact")