from django.urls import path
from .views import TourListView, TourDetailView

app_name = 'tour'

urlpatterns = [
    path('', TourListView.as_view(), name='tour_list'),
    path('<int:pk>/', TourDetailView.as_view(), name='tour_detail'),
]