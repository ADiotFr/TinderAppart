from django import forms
from .models import Property, Tenant


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'


class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = '__all__'
