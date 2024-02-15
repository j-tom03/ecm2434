from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    coins = models.IntegerField(default=0)
    completed_challenges = models.IntegerField(default=0)

    def __str__(self):
        return self.username

