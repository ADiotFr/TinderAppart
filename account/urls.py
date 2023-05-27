# Import the authentication views module from Django's built-in authentication system.
from django.contrib.auth import views as auth_views

# Import the path function from Django's url handling module.
from django.urls import path

# Define the URL patterns for this application.
urlpatterns = [
    # Map the '/login/' URL to the LoginView. This handles user login.
    path('login/', auth_views.LoginView.as_view(), name='login'),

    # Map the '/logout/' URL to the LogoutView. This handles user logout.
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
