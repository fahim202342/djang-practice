from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required   
from CalorieCounter.models import *
from CalorieCounter.forms import *


def register_page(request):
    if request.method == 'POST':
        form_data = RegistrationForm(request.POST)
        
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Registration Successfully')
            return redirect('login_page')
    
    form_data = RegistrationForm()

    context = {
        'form_data': form_data,
        'form_title': 'User Registration Form',
        'form_btn': 'Register',
    }

    return render(request, 'master/base-form.html', context)


def login_page(request):  
    if request.method == 'POST':
        form_data = LoginForm(request, data=request.POST)

        if form_data.is_valid():
            user = form_data.get_user()

            login(request, user)

            messages.success(request, 'Login Successfully')
            return redirect('dashboard_page')
    
    form_data = LoginForm()

    context = {
        'form_data': form_data,
        'form_title': 'User Login Form',
        'form_btn': 'Login',
    }

    return render(request, 'master/base-form.html', context)


@login_required
def logout_page(request):
    logout(request)
    return redirect('login_page')


@login_required
def dashboard_page(request):
    return render(request, 'dashboard.html')

@login_required
def profile_page(request):
    return render(request, 'profile.html')

@login_required
def update_profile(request):
    try:
        current_user = request.user.user_info
    except:
        current_user = None
    if request.method == 'POST':
        form_data = UpdateProfileForm(request.POST, instance=current_user)

        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.user = request.user
            
            weight = data.weight
            height = data.height
            age = data.age
            if data.gender == "Male":
                #66.47+(13.75 x weight in kg) + (5.003 x height in cm) - (6.755 x age in years)
                bmr_calculation = 66.47+(13.75 * weight) + (5.003 * height) - (6.755 * age)
                
            else:
                #BMR=655.1+(9.563 x weight in kg)+(1.850 x height in cm) - (4.676 x age in years)
                bmr_calculation = 655.1+(9.563 * weight)+(1.850 * height) - (4.676 * age)
        
            data.bmr = bmr_calculation
            data.save()

            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile_page')
    
    form_data = UpdateProfileForm(instance=current_user)
    context = {
        'form_data': form_data,
        'form_title': 'Update Profile',
        'form_btn': 'Update',
    }
    
    return render(request, 'master/base-form.html', context)

def consumed_calories_list(request):
    consumed_data = ConsumedCalories.objects.filter(create_by=request.user)

    context = {
        'consumed_data': consumed_data
    }

    return render(request, 'consumed_calories_list.html', context)

def add_calorie(request):
    if request.method == 'POST':
        form_data = ConsumedCalorieForm(request.POST)

        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.create_by = request.user
            data.save()

            messages.success(request, 'Successfully')
            return redirect('consumed_calories_list') 
    
    form_data = ConsumedCalorieForm()
    context = {
        'form_data': form_data,
        'form_title': 'Add Calories Info',
        'form_btn': 'Add Calories',
    }
    return render(request, 'master/base-form.html', context)


def update_calorie(request, t_id):
    try:
        calorie = ConsumedCalories.objects.get(id=t_id)
    except ConsumedCalories.DoesNotExist:
        messages.error(request, 'Calorie not found')
        return redirect('consumed_calories_list')

    if request.method == 'POST':
        form_data = ConsumedCalorieForm(request.POST, instance=calorie)

        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.create_by = request.user
            data.save()

            messages.success(request, 'Successfully')
            return redirect('consumed_calories_list') 
    
    form_data = ConsumedCalorieForm(instance=calorie)
    context = {
        'form_data': form_data,
        'form_title': 'Update Calories Info',
        'form_btn': 'Update Calories',
    }
    return render(request, 'master/base-form.html', context)

def delete_calorie(request, t_id):
    try:
        calorie = ConsumedCalories.objects.get(id=t_id)
    except ConsumedCalories.DoesNotExist:
        messages.error(request, 'Calorie not found')
        return redirect('consumed_calories_list')

    calorie.delete()
    messages.success(request, 'Successfully')
    return redirect('consumed_calories_list')
