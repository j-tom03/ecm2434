from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager


# Create your models here


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, primary_key=True, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    image = models.CharField(max_length=200, default="dog")
    coins = models.IntegerField(default=0)
    completed_challenges = models.CharField(default="", max_length=2000)
    setter = models.BooleanField(default=False)
    institution = models.BooleanField(default=False)
    garden = models.CharField(max_length=160, default=f"{'0' * 160}")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now=True)
    gdpr = models.BooleanField(default=False)

    objects = CustomUserManager()

    REQUIRED_FIELDS = ["email"]
    USERNAME_FIELD = "username"
    is_anonymous = False
    is_authenticated = True

    def __str__(self):
        return f"{self.username}{', setter' if self.setter == True else ''}" \
               f"{', institution' if self.institution == True else ''}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class Challenge(models.Model):
    challenge_ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(default="")
    coins = models.IntegerField()
    challenge_setter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class transport_challenge(models.Model):
    challenge_ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    start_point = models.CharField(max_length=200)
    end_point = models.CharField(max_length=200)
    distance_covered = models.FloatField(default=0.00)

    def __str__(self):
        return self.title


class CompleteChallenge(models.Model):
    challenge_ID = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.challenge_ID.title + " " + self.user.username


class FactMatchModel(models.Model):
    # the entire text unedited
    text = models.TextField(default="")
    # the words in the text to be filled in represented by a string of nums with commas eg *1,4,6,11*
    words = models.TextField(default="")
    coins = models.IntegerField(default=30)
    setter = models.ForeignKey(User, on_delete=models.CASCADE)


class CompleteTransportChallenge(models.Model):
    challenge_ID = models.ForeignKey(transport_challenge, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    distance = models.FloatField(default=0.00)

    def __str__(self):
        return self.challenge_ID.title + " " + self.user.username


