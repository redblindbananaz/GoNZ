from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Agent(models.Model):
    # One-to-one relationship with the built-in User model in Django
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    
    # Default values for department and position fields
    department = models.CharField(max_length=100, default='Agent')
    position = models.CharField(max_length=100, default='Agent')
    
    # Fields representing attributes of an agent
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    bio = models.TextField()
    
     # Field to store the agent's profile picture
    profile_pic = models.ImageField(upload_to='profiles/', null=True, blank=True, default = 'profiles/default.jpg')

    # Return a string representation of the agent object (the agent's name)
    def __str__(self):
        return self.name
    
    # Return the URL for the agent's detail view based on the agent's primary key (pk)
    def get_absolute_url(self):
        return reverse("agent_detail",kwargs={"pk": self.pk})