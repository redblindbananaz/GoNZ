from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home.html'
    
    # to check if a user is authenticated or not, if the user is logged in then it will return the username
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['username'] = self.request.user
        return context

class LoginView(View):
    def get(self, request):
        return render(request, 'home/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:home')  #If user exist it returns to home page
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('home:login')
        # Otherwise, return an 'invalid login' error message.

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'home/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please check the form.')
        return render(request, 'home/register.html', {'form': form})
