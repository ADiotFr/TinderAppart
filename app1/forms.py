from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Property, Tenant, Match


# Form for adding or updating Property instances.
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ['user']  # Exclude 'user' field from the form.


# Form for adding or updating Tenant instances.
class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        exclude = ['user']  # Exclude 'user' field from the form.


# Form for adding or updating Match instances.
class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['tenant', 'property', 'message']  # Only include these fields in the form.


# Form for tenants to specify their housing preferences.
class TenantPreferenceForm(forms.Form):
    min_budget = forms.DecimalField(label="Minimum price", required=False)
    max_budget = forms.DecimalField(label="Maximum price", required=False)
    min_bedrooms = forms.IntegerField(label="Minimum bedrooms", required=False)
    max_bedrooms = forms.IntegerField(label="Maximum bedrooms", required=False)
    min_bathrooms = forms.IntegerField(label="Minimum bathrooms", required=False)
    max_bathrooms = forms.IntegerField(label="Maximum bathrooms", required=False)


# Form for property owners to specify their property preferences.
class OwnerPreferenceForm(forms.Form):
    min_budget = forms.DecimalField(label="Minimum price", required=False)
    max_budget = forms.DecimalField(label="Maximum price", required=False)
    min_bedrooms = forms.IntegerField(label="Minimum bedrooms", required=False)
    max_bedrooms = forms.IntegerField(label="Maximum bedrooms", required=False)
    min_bathrooms = forms.IntegerField(label="Minimum bathrooms", required=False)
    max_bathrooms = forms.IntegerField(label="Maximum bathrooms", required=False)


# Form for registering new users.
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Only include these fields in the form.
