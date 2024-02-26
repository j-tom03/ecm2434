from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.statistics, name='statistics'),
    path('', views.index, name='index')
    ]