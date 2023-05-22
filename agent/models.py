from django.db import models

# Create your models here.

class Agent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    bio = models.TextField()

    def __str__(self):
        return self.name