from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CareSeekerSignupForm

def care_seeker_signup(request):
    if request.method == 'POST':
        form = CareSeekerSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after signup
    else:
        form = CareSeekerSignupForm()
    return render(request, 'users/signup_careseeker.html', {'form': form})

def home(request):
    return render(request, 'users/home.html') 