from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Tour

# Create your views here.

class TourListView(ListView):
    model = Tour
    template_name = 'tour/tour_list.html'
    context_object_name = 'tours'

class TourDetailView(DetailView):
    model = Tour
    template_name = 'tour/tour_detail.html'
    context_object_name = 'tour'