from django.db import models

# Create your models here


class User(models.Model):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    coins = models.IntegerField(default=0)
    completed_challenges = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class challenge(models.Model):
    challenge_ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    coins = models.IntegerField()
    challenge_setter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

