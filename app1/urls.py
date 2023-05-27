from django.urls import path
from . import views

# Define the namespace for this application's URLs.
app_name = 'app1'

# Define the URL patterns for this application.
urlpatterns = [
    path('', views.home, name='home'),  # The home page.
    path('property_list/', views.property_list, name='property_list'),  # List of properties.
    path('property_create/', views.property_create, name='property_create'),  # Page to create a new property.
    path('property/<int:property_id>/', views.property_detail, name='property_detail'),
    # Detail view for a specific property.
    path('property/<int:property_id>/update/', views.property_update, name='property_update'),
    # Page to update a specific property.
    path('property/<int:property_id>/delete/', views.property_delete, name='property_delete'),
    # Action to delete a specific property.
    path('tenant_list/', views.tenant_list, name='tenant_list'),  # List of tenants.
    path('tenant_create/', views.tenant_create, name='tenant_create'),  # Page to create a new tenant.
    path('tenant_detail/<int:pk>/', views.tenant_detail, name='tenant_detail'),  # Detail view for a specific tenant.
    path('tenant_update/<int:pk>/', views.tenant_update, name='tenant_update'),  # Page to update a specific tenant.
    path('tenant_delete/<int:pk>/', views.tenant_delete, name='tenant_delete'),  # Action to delete a specific property.
    path('register/', views.register, name='register'),  # User registration page.
    path('login/', views.user_login, name='login'),  # User login page.
    path('profile/', views.profile, name='profile'),  # User profile page.
    path('logout/', views.logout_view, name='logout'),  # User logout action.
    path('match/', views.match, name='match'),  # Page for matching tenants and properties.


]
