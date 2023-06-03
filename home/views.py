from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home.html'
    
    # Retrieves the context data for the home view
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Check if the user is authenticated and add the username to the context
        if self.request.user.is_authenticated:
            context['username'] = self.request.user
        return context

class LoginView(View):
    def get(self, request):
        return render(request, 'home/login.html')

    def post(self, request):
        # Retrieve the username and password from the request
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
         # If the user exists, log them in and redirect to the home page
        if user is not None:
            login(request, user)
            return redirect('home:home') 
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('home:login')
        # Otherwise, return an 'invalid login' error message.

class RegisterView(View):
    def get(self, request):
        # Create an instance of the UserCreationForm
        form = UserCreationForm()
        # Render the registration page with the form
        return render(request, 'home/register.html', {'form': form})

    def post(self, request):
        # Create an instance of the UserCreationForm with the form data from the request
        form = UserCreationForm(request.POST)
        
        # If the form is valid, save the user, log them in, display a success message, and redirect to the home page
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home:home')
        else:
            messages.error(request, 'Registration failed. Please check the form.')
        return render(request, 'home/register.html', {'form': form})
