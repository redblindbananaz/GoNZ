from django.contrib.auth.models import AbstractUser, Group
from django.db import models

# Create your models here.

class Agent(AbstractUser):
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    bio = models.TextField()
    is_agent = models.BooleanField(default=True)

    def __str__(self):
        return self.name