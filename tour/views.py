from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.http import request

from .models import Tour

# Create your views here.

class TourListView(ListView):
    model = Tour
    template_name = 'tour/tour_list.html'
    context_object_name = 'tours'
    paginate_by = 3
    ordering = ['-id']  # Specify the ordering field for consistent pagination, in this case the last one first.

class TourDetailView(DetailView):
    model = Tour
    template_name = 'tour/tour_detail.html'
    context_object_name = 'tour'