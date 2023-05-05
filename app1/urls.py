from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('', views.home, name='home'),
    path('property_list/', views.property_list, name='property_list'),
    path('property_detail/<int:pk>/', views.property_detail, name='property_detail'),
    path('property_create/', views.property_create, name='property_create'),
    path('property_update/<int:pk>/', views.property_update, name='property_update'),
    path('property_delete/<int:pk>/', views.property_delete, name='property_delete'),
    path('tenant_list/', views.tenant_list, name='tenant_list'),
    path('tenant_detail/<int:pk>/', views.tenant_detail, name='tenant_detail'),
    path('tenant_create/', views.tenant_create, name='tenant_create'),
    path('tenant_update/<int:pk>/', views.tenant_update, name='tenant_update'),
    path('tenant_delete/<int:pk>/', views.tenant_delete, name='tenant_delete'),
]
