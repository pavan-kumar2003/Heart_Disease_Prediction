from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from .models import UserPrediction
# predictor/views.py
import matplotlib.pyplot as plt
import io
import urllib, base64

from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Register View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account created successfully! Welcome, {user.username}!')
            return redirect('login')
        else:
            messages.error(request, 'There was an error with your registration. Please try again.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
#logout page redirection 
def logout_view(request):
    logout(request)  # Logs out the user
    return redirect('login')  # Redirect to the login page or home page

# Profile View
@login_required(login_url='login')
def profile(request):
    predictions = UserPrediction.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'profile.html', {'user': request.user, 'predictions': predictions})


from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


# predictor/views.py
from django.core.mail import send_mail

def send_notification(user_email, prediction):
    send_mail(
        'Heart Disease Prediction Result',
        f'Your prediction result: {prediction}',
        'from@example.com',
        [user_email],
        fail_silently=False,
    )
# heart_disease/views.py
import joblib
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import HeartDiseaseForm
from .models import UserPrediction
from django.contrib import messages

# Load the trained model and scaler
model = joblib.load('heart_disease_model.pkl')  # Update with the correct path
scaler = joblib.load('scaler.pkl')               # Update with the correct path

@login_required(login_url='login')  # these will redirect to login page if user not loged in
def predict(request):
    if request.method == 'POST':
        form = HeartDiseaseForm(request.POST)
        if form.is_valid():
            # Collect and preprocess input data
            input_data = [
                form.cleaned_data['age'],
                form.cleaned_data['sex'],
                form.cleaned_data['cp'],
                form.cleaned_data['trestbps'],
                form.cleaned_data['chol'],
                form.cleaned_data['fbs'],
                form.cleaned_data['restecg'],
                form.cleaned_data['thalach'],
                form.cleaned_data['exang'],
                form.cleaned_data['oldpeak'],
                form.cleaned_data['slope'],
                form.cleaned_data['ca'],
                form.cleaned_data['thal']
            ]
            
            # Scale the input data
            input_data_scaled = scaler.transform([input_data])
            
            # Make prediction
            prediction = model.predict(input_data_scaled)
            result = 'Heart Disease' if prediction[0] == 1 else 'No Heart Disease'
            messages.success(request, f'Prediction Result: {result}')

            # Save the prediction to the database
            UserPrediction.objects.create(
                user=request.user,
                input_data=input_data,
                prediction=result
            )
            return render(request, 'predict.html', {'form': form, 'result': result})
    else:
        form = HeartDiseaseForm()
    
    return render(request, 'predict.html', {'form': form})

from django.shortcuts import render
from .forms import HealthIndicatorForm
import numpy as np

model2 = joblib.load('heart_indicator_model.pkl')  # Update with the correct path
scaler2 = joblib.load('scaler2.pkl') 

def symptom(request):
    if request.method == 'POST':
        form = HealthIndicatorForm(request.POST)
        
        if form.is_valid():
            age = form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            HighBP = form.cleaned_data['HighBP']
            HighChol = form.cleaned_data['HighChol']
            CholCheck = form.cleaned_data['CholCheck']
            BMI = form.cleaned_data['BMI']
            Smoker = form.cleaned_data['Smoker']
            Stroke = form.cleaned_data['Stroke']
            Diabetes = form.cleaned_data['Diabetes']
            PhysActivity = form.cleaned_data['PhysActivity']
            HvyAlcoholConsump = form.cleaned_data['HvyAlcoholConsump']
            AnyHealthcare = form.cleaned_data['AnyHealthcare']
            NoDocbcCost = form.cleaned_data['NoDocbcCost']
            GenHlth = form.cleaned_data['GenHlth']
            MentHlth = form.cleaned_data['MentHlth']
            PhysHlth = form.cleaned_data['PhysHlth']
            DiffWalk = form.cleaned_data['DiffWalk']
            
            data = [HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, Diabetes, PhysActivity, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth, MentHlth, PhysHlth, DiffWalk, sex, age]
            
            input_data_scaled = scaler2.transform([data])
            
            # Make prediction
            prediction = model2.predict(input_data_scaled)
            result = 'Heart Disease' if prediction[0] == 1 else 'No Heart Disease'
            messages.success(request, f'Prediction Result: {result}')

            # Save the prediction to the database
            UserPrediction.objects.create(
                user=request.user,
                input_data=data,
                prediction=result
            )
            return render(request, 'symptom.html', {'form': form, 'result': result})
    else:
        form = HealthIndicatorForm()

    return render(request, 'symptom.html', {'form': form})

from .forms import BMICalculatorForm
def bmi(request):
    bmi = None
    category = None

    if request.method == 'POST':
        form = BMICalculatorForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data['height'] / 100  # Convert cm to meters
            weight = form.cleaned_data['weight']
            bmi = weight / (height ** 2)

            if bmi < 18.5:
                category = 'Underweight'
            elif 18.5 <= bmi < 24.9:
                category = 'Normal weight'
            elif 25 <= bmi < 29.9:
                category = 'Overweight'
            else:
                category = 'Obesity'
    else:
        form = BMICalculatorForm()

    return render(request, 'bmi.html', {'form': form, 'bmi': bmi, 'category': category})
