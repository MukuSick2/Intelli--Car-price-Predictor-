from django.shortcuts import render,HttpResponse

""" ye codes koi bhi nhi dekh paayega """
"Create your views here."
"""def index(request):
    return render(request,"home.html")
    # return HttpResponse("this is home page")
def about(request):
    return HttpResponse("this is home page")
def login(request):
    return  render(request,"login.html")
def signup(request):
    return render(request, 'signup.html')"""
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from .forms import LoginForm

# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')  # Redirect to home page after successful login
#             else:
#                 # Handle invalid login
#                 return render(request, 'login.html', {'form': form, 'error_message': 'Invalid username or password'})
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})

# def logout(request):
#     logout(request)
#     return redirect('login')  # Redirect to login page after logout

from django.shortcuts import render, redirect
from.models import LoginForm,signupForm
# from.forms import CarForm, LoginForm
import pickle
import pandas as pd
import numpy as np
from django.contrib.sessions.backends.db import SessionStore
from django.contrib import messages
from django.http import JsonResponse
from datetime import datetime

def login(request):
    

    # if request.method == 'POST':
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         l = form.save()
    #         return render(request, 'index.html',l=l)
    # else:
    #     form = LoginForm()
    # return render(request, 'index.html', {'form': form})
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = LoginForm(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or the previous page
            return redirect('index.html')
        else:
            # Display an error message
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    
def signup(request):
     if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        signupForm.objects.create(username=username, email=email, password=password)
        messages.success(request, 'Account created successfully. Please login.')
        return redirect('login')
     else:
         return render(request, 'signup.html')

car= pd.read_csv('Cleaned_Car_data.csv')
model = pickle.load(open('LinearRegressionModel.pkl','rb'))
def index(request):
            
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_types = car['fuel_type'].unique()
    kms_driven = sorted(car['kms_driven'].unique())
   

    companies.insert(0, 'Select Company')
    return render(request, 'index.html', {'company': companies, 'car_models': car_models, 'years': years, 'fuel_types': fuel_types, 'kms_driven':kms_driven})
    

from .models import models
def home(request):
    return render(request,'home.html')
def predict(request):
    # if request.method=='POST':
    # companies = sorted(car['company'].unique())
    # car_models = sorted(car['name'].unique())
    # years = sorted(car['year'].unique(), reverse=True)
    # fuel_types = car['fuel_type'].unique()
    # kms_driven = sorted(car['kms_driven'].unique())
    # prediction = predict(request.POST)

    # companies.insert(0, 'Select Company')
    # return JsonResponse({'prediction': prediction})
        company = request.POST.get('company')
        car_model = request.POST.get('car_model')
        year = int(request.POST.get('year'))
        fuel_type = request.POST.get('fuel_type')
        kms_driven = float(request.POST.get('kilo_driven'))

        # Prepare the input data for the ML model
        # (Replace the following line with your actual preprocessing steps)
        # car= pd.read_csv('Cleaned_Car_data.csv')
        input_data=[company,car_model,year,fuel_type,kms_driven]

        # Make the prediction
        prediction = model.predict(input_data)[0]

        return render(request, 'index.html', {'prediction': prediction})


# def index(request):
#     name= request.GET['name']
#     company= request.GET['company']
#     year= request.GET['year']
#     price= request.GET['price']
#     kms_driven= request.GET['kms_driven']
#     fuel_type = request.GET['fuel_type']
#     return render(request,"index.html")

from django.shortcuts import render
from django.contrib.auth import authenticate, login

def login_f(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or the previous page
            return redirect('index.html')
        else:
            # Display an error message
            error_message = 'Invalid username or password'
            return render(request, 'home.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # Use Django's built-in User model
from django.contrib import messages  # For user-friendly messages

def signup(request):
    return render(request,'signup.html')
