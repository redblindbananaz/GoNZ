from django.apps import AppConfig


class AgentConfig(AppConfig):
    #The default_auto_field attribute is set to use BigAutoField as the default auto-generated primary key field for the app's models. 
    default_auto_field = "django.db.models.BigAutoField"
    name = "agent"
