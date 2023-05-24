from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    department = models.CharField(max_length=100, default='Agent')
    position = models.CharField(max_length=100, default='Agent')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    bio = models.TextField()

    def __str__(self):
        return self.name