from django.urls import path
from .views import HomeView, LoginView, RegisterView


app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]