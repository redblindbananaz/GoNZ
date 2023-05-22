from django.urls import path
from .views import AgentListView, AgentDetailView

app_name = 'agent'

urlpatterns = [ 
    path('', AgentListView.as_view(), name='agent_list'),
    path('<int:pk>/', AgentDetailView.as_view(), name='agent_detail'),
]