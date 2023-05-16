from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Property, Tenant, Match


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ['user']


class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        exclude = ['user']


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['tenant', 'property', 'message']


class TenantPreferenceForm(forms.Form):
    min_budget = forms.DecimalField(label="Minimum price", required=False)
    max_budget = forms.DecimalField(label="Maximum price", required=False)
    min_bedrooms = forms.IntegerField(label="Minimum bedrooms", required=False)
    max_bedrooms = forms.IntegerField(label="Maximum bedrooms", required=False)
    min_bathrooms = forms.IntegerField(label="Minimum bathrooms", required=False)
    max_bathrooms = forms.IntegerField(label="Maximum bathrooms", required=False)


class OwnerPreferenceForm(forms.Form):
    min_budget = forms.DecimalField(label="Minimum price", required=False)
    max_budget = forms.DecimalField(label="Maximum price", required=False)
    min_bedrooms = forms.IntegerField(label="Minimum bedrooms", required=False)
    max_bedrooms = forms.IntegerField(label="Maximum bedrooms", required=False)
    min_bathrooms = forms.IntegerField(label="Minimum bathrooms", required=False)
    max_bathrooms = forms.IntegerField(label="Maximum bathrooms", required=False)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
