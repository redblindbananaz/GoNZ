from django.db import models
from django.urls import reverse

# Create your models here.

class Tour(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    agent = models.ForeignKey('agent.Agent', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Add the price field
    image = models.ImageField(upload_to='tour_images/')  # Add the image field


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("tour_detail",kwargs={"pk": self.pk})
