# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Property, Tenant
from .forms import PropertyForm, TenantForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def property_list(request):
    properties = Property.objects.all()
    context = {'property': properties}
    return render(request, 'app1/property_list.html', context)


def property_detail(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    return render(request, 'app1/property_detail.html', {'property': property})


def tenant_list(request):
    tenants = Tenant.objects.all()
    context = {'tenant': tenants}
    return render(request, 'app1/tenant_list.html', context)


def tenant_detail(request, pk):
    tenant = Tenant.objects.get(pk=pk)
    context = {'tenant': tenant}
    return render(request, 'app1/tenant_detail.html', context)


@login_required
def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            property = form.save(commit=False)
            property.user = request.user
            property.save()
            return redirect('app1:profile')
    else:
        form = PropertyForm()

    return render(request, 'app1/property_form.html', {'form': form})


@login_required
def property_update(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    if request.method == "POST":
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('app1:profile')
    else:
        form = PropertyForm(instance=property)
    return render(request, 'app1/property_form.html', {'form': form})


@login_required
def property_delete(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    if request.method == "POST":
        property.delete()
        return redirect('app1:profile')
    return render(request, 'app1/property_confirm_delete.html', {'property': property})


@login_required
def tenant_create(request):
    if request.method == "POST":
        form = TenantForm(request.POST)
        if form.is_valid():
            tenant = form.save(commit=False)
            tenant.user = request.user
            tenant.save()
            return redirect('app1:profile')
    else:
        form = TenantForm()

    tenant_exists = Tenant.objects.filter(user=request.user).exists()

    return render(request, 'app1/tenant_form.html', {'form': form, 'tenant_exists': tenant_exists})


def tenant_update(request, pk):
    tenant = Tenant.objects.get(pk=pk)
    if request.method == 'POST':
        form = TenantForm(request.POST, instance=tenant)
        if form.is_valid():
            form.save()
            return redirect('app1:profile')
    else:
        form = TenantForm(instance=tenant)
    context = {'form': form}
    return render(request, 'app1/tenant_form.html', context)


def tenant_delete(_, pk):
    tenant = Tenant.objects.get(pk=pk)
    tenant.delete()
    return redirect('app1:profile')


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'app1/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')  # or your desired page after login
        else:
            return render(request, 'app1/login.html', {'error': 'Invalid login credentials'})

    return render(request, 'app1/login.html')


@login_required
def profile(request):
    tenants = Tenant.objects.filter(user=request.user)
    properties = Property.objects.filter(user=request.user)
    return render(request, 'app1/profile.html', {'properties': properties, 'tenants': tenants})


def logout_view(request):
    logout(request)
    return redirect('app1:login')


@login_required
def match(request):
    properties = Property.objects.filter(user=request.user)
    tenants = Tenant.objects.filter(user=request.user)

    property_matches = []
    for property in properties:
        matching_tenants = Tenant.objects.filter(budget__gte=property.price, bedrooms__lte=property.bedrooms, bathrooms__lte=property.bathrooms)
        for tenant in matching_tenants:
            if tenant.user != property.user:
                property_matches.append((property, tenant))

    tenant_matches = []
    for tenant in tenants:
        matching_properties = Property.objects.filter(price__lte=tenant.budget, bedrooms__gte=tenant.bedrooms, bathrooms__gte=tenant.bathrooms)
        for property in matching_properties:
            if property.user != tenant.user:
                tenant_matches.append((property, tenant))

    return render(request, 'app1/match.html', {'property_matches': property_matches, 'tenant_matches': tenant_matches})
