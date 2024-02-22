from django.db import models

# Create your models here.
class Fact(models.Model):
    fact = models.CharField(max_length=200)
    def __str__(self):
        return self.fact
    
