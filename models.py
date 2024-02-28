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
    institution = models.BooleanField(default=False)
    garden = models.CharField(max_length=200, default="default_garden")

    def __str__(self):
        return f"{self.username}{', setter' if self.setter == True else ''}" \
               f"{', institution' if self.institution == True else ''}"


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
    image_proof = models.ImageField()

    def __str__(self):
        return self.challenge_ID.title + " " + self.user.username


class completeCycleChallenge(models.Model):
    challenge_ID = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_point = models.CharField(label="Start Point")
    end_point = models.CharField(label="End Point")

    def __str__(self):
        return self.challenge_ID.title + " " + self.user.username
