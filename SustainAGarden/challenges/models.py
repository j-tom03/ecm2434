from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('The username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=200, primary_key=True, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/default.jpg')
    # these should be stored hashed not raw
    password = models.CharField(max_length=200, blank=False)
    coins = models.IntegerField(default=0)
    completed_challenges = models.CharField(default="", max_length=10)
    setter = models.BooleanField(default=False)
    institution = models.BooleanField(default=False)
    garden = models.CharField(max_length=200, default="default_garden")
    last_login = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "username"
    PASSWORD_FIELD = "password"
    EMAIL_FIELD = "email"
    is_anonymous = False
    is_authenticated = True
    objects = CustomUserManager()


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

    def __str__(self):
        return self.challenge_ID.title + " " + self.user.username
