from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Agent

# Create your views here.

class AgentListView(ListView):
    model = Agent
    template_name = 'agent_list.html'
    context_object_name = 'agents'

class AgentDetailView(DetailView):
    model = Agent
    template_name = 'agent_detail.html'
    context_object_name = 'agent'
