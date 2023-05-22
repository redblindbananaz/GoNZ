from django.shortcuts import render
from django.views.generic import ListView
from .models import Tour

# Create your views here.

class TourListView(ListView):
    model = Tour
    template_name = 'tour_list.html'
    context_object_name = 'tour_list'
    paginate_by = 10