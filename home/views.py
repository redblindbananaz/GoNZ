from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home.html'

class LoginView(View):
    def get(self, request):
        return render(request, 'home/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:home')  # Replace 'tour-list' with the URL name of the tour list page
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('home:login')
