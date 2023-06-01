from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Agent
from django.contrib.auth.models import Group

# Create your views here.

class AgentListView(ListView):
    model = Agent
    template_name = 'agent/agent_list.html'
    context_object_name = 'agents'
    
    

class AgentDetailView(DetailView):
    model = Agent
    template_name = 'agent/agent_detail.html'
    context_object_name = 'agent'
