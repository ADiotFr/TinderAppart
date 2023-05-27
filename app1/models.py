from django.db import models
from django.contrib.auth.models import User


# Tenant model representing a tenant in the application.
class Tenant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    bedrooms = models.IntegerField(blank=True, null=True)
    bathrooms = models.IntegerField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='tenants_photos', blank=True, null=True)
    objects = models.Manager()

    # Returns the name of the tenant as the string representation of the tenant object.
    def __str__(self):
        return self.name


# Property model representing a property in the application.
class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bedrooms = models.IntegerField(blank=True, null=True)
    bathrooms = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='property_photos', blank=True, null=True)
    objects = models.Manager()

    # Returns the name of the property as the string representation of the property object.
    def __str__(self):
        return self.name


# Match model representing a match between a tenant and a property.
class Match(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    message = models.TextField()
    objects = models.Manager()

    # Returns a formatted string representing the match as the string representation of the match object.
    def __str__(self):
        return f"{self.tenant} matched with {self.property}"
