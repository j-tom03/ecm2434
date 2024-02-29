from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager


# Create your models here


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, primary_key=True, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/default.jpg')
    # these should be stored hashed not raw
    coins = models.IntegerField(default=0)
    completed_challenges = models.CharField(default="", max_length=10)
    setter = models.BooleanField(default=False)
    institution = models.BooleanField(default=False)
    garden = models.CharField(max_length=160, default=f"{'0' * 160}")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now=True)

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
    transport = models.BooleanField(default=False)
    description = models.TextField(default="")
    coins = models.IntegerField()
    # only used if the challenges is a transport challenge, use what three words?
    start_point = models.CharField(default="000, 000, 000", max_length=200)
    end_point = models.CharField(default="000, 000, 000", max_length=200)
    challenge_setter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class CompleteChallenge(models.Model):
    challenge_ID = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.challenge_ID.title + " " + self.user.username
