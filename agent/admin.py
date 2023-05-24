from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Agent    

# Register your models here.

class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'position')


admin.site.register(Agent, AgentAdmin)  