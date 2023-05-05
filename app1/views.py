# Create your views here.
from django.shortcuts import render, redirect
from .models import Property, Tenant
from .forms import PropertyForm, TenantForm


def property_list(request):
    properties = Property.objects.all()
    context = {'properties': properties}
    return render(request, 'myproject/property_list.html', context)


def property_detail(request, pk):
    property = Property.objects.get(pk=pk)
    context = {'property': property}
    return render(request, 'myproject/property_detail.html', context)


def tenant_list(request):
    tenants = Tenant.objects.all()
    context = {'tenants': tenants}
    return render(request, 'myproject/tenant_list.html', context)


def tenant_detail(request, pk):
    tenant = Tenant.objects.get(pk=pk)
    context = {'tenant': tenant}
    return render(request, 'myproject/tenant_detail.html', context)


def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    context = {'form': form}
    return render(request, 'myproject/property_form.html', context)


def property_update(request, pk):
    property = Property.objects.get(pk=pk)
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm(instance=property)
    context = {'form': form}
    return render(request, 'myproject/property_form.html', context)


def property_delete(_, pk):
    property = Property.objects.get(pk=pk)
    property.delete()
    return redirect('property_list')


def tenant_create(request):
    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tenant_list')
    else:
        form = TenantForm()
    context = {'form': form}
    return render(request, 'myproject/tenant_form.html', context)


def tenant_update(request, pk):
    tenant = Tenant.objects.get(pk=pk)
    if request.method == 'POST':
        form = TenantForm(request.POST, instance=tenant)
        if form.is_valid():
            form.save()
            return redirect('tenant_list')
    else:
        form = TenantForm(instance=tenant)
    context = {'form': form}
    return render(request, 'myproject/tenant_form.html', context)


def tenant_delete(_, pk):
    tenant = Tenant.objects.get(pk=pk)
    tenant.delete()
    return redirect('tenant_list')


def home(request):
    return render(request, 'home.html')
