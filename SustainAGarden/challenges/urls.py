from django.urls import path, re_path
from . import views

urlpatterns = [
    path('view/', views.statistics, name='statistics'),
    path('set-challenge/', views.set_challenge, name='setChallenge'),
    path('all-challenges/', views.all_challenges, name='allChallenges'),
    path('gdpr/', views.gdpr, name='gdpr'),
    path('update_coins/', views.update_coins, name='updateCoins'),
    path('store_garden/', views.store_garden, name='storeGarden'),
    re_path(r'.*\.jpg', views.profile_image, name='profileImage'),
    path('', views.index, name='index')
    ]