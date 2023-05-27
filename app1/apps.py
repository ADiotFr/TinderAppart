from django.apps import AppConfig


# Configuration for the app1 application.
class App1Config(AppConfig):
    # Specifies the type of auto-created primary key fields.
    default_auto_field = "django.db.models.BigAutoField"

    # The name of the application.
    name = "app1"
