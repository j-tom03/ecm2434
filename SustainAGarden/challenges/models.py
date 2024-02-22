from django.db import models

# Create your models here


class User(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
    email = models.EmailField(max_length=200)
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/default.jpg')
    # these should be stored hashed not raw
    password = models.CharField(max_length=200)
    coins = models.IntegerField(default=0)
    completed_challenges = models.IntegerField(default=0)
    setter = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Challenge(models.Model):
    challenge_ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    coins = models.IntegerField()
    challenge_setter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class completeChallenge(models.Model):
    challenge_ID = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.challenge_ID.title + " " + self.user.username

