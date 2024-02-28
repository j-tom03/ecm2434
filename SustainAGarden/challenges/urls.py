from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.statistics, name='statistics'),
    path('set-challenge/', views.set_challenge, name='setChallenge'),
    path('all-challenges/', views.all_challenges, name='allChallenges'),
    path('', views.index, name='index')
    ]