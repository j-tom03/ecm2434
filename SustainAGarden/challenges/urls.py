from django.urls import path, re_path
from . import views

urlpatterns = [
    path('view/', views.statistics, name='statistics'),
    path('set-challenge/', views.set_challenge, name='setChallenge'),
    path('all-challenges/', views.all_challenges, name='allChallenges'),
    re_path(r'.*\.jpg', views.profile_image, name='profileImage'),
    path('', views.index, name='index')
    ]