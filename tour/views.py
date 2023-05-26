from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .models import Tour

# Create your views here.

class TourListView(ListView):
    model = Tour
    template_name = 'tour/tour_list.html'
    context_object_name = 'tours'
    paginate_by = 3
    ordering = ['-id']  # Specify the ordering field for consistent pagination, in this case the last one first.
    
    def get_queryset(self):
        queryset = super().get_queryset()
        paginator = Paginator(queryset, self.paginate_by)
        page_number = self.request.GET.get('page')
        return paginator.get_page(page_number)

class TourDetailView(DetailView):
    model = Tour
    template_name = 'tour/tour_detail.html'
    context_object_name = 'tour'