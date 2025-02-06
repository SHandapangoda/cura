from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CareSeekerSignupForm, CareProviderSignupForm, GuardianSignupForm
from .models import User
from django.contrib import messages
from django.core import signing
from django.conf import settings
from django.core.mail import send_mail

from django.template.loader import render_to_string
from django.utils.html import strip_tags

def home(request):
    return render(request, 'users/home.html')

def landing_page(request):
    return render(request, 'users/landing_page.html')

def care_seeker_dashboard(request):
    return render(request, 'users/care_seeker_dashboard.html')

def care_provider_dashboard(request):
    return render(request, 'users/care_provider_dashboard.html')

def guardian_dashboard(request):
    return render(request, 'users/guardian_dashboard.html')

def care_seeker_signup(request):
    if request.method == 'POST':
        form = CareSeekerSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            # Generate a verification token
            token = signing.dumps({'user_id': user.id})
            
            # Send verification email
            subject = 'Verify Your Email Address'
            verification_url = request.build_absolute_uri(f'/users/verify-email/{token}/')
            html_message = render_to_string('users/verification_email.html', {'verification_url': verification_url})
            plain_message = strip_tags(html_message)
            send_mail(subject, plain_message, settings.DEFAULT_FROM_EMAIL, [user.email], html_message=html_message)
            
            return redirect('home')  # Redirect to home page after signup
    else:
        form = CareSeekerSignupForm()
    return render(request, 'users/care_seeker_signup.html', {'form': form})

def care_provider_signup(request):
    if request.method == 'POST':
        form = CareProviderSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Send verification email
            subject = 'Verify Your Email Address'
            html_message = render_to_string('users/verification_email.html', {'user': user})
            plain_message = strip_tags(html_message)
            send_mail(subject, plain_message, settings.DEFAULT_FROM_EMAIL, [user.email], html_message=html_message)
            return redirect('home')  # Redirect to home page after signup
    else:
        form = CareProviderSignupForm()
    return render(request, 'users/care_provider_signup.html', {'form': form})

def guardian_signup(request):
    if request.method == 'POST':
        form = GuardianSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Send verification email
            subject = 'Verify Your Email Address'
            html_message = render_to_string('users/verification_email.html', {'user': user})
            plain_message = strip_tags(html_message)
            send_mail(subject, plain_message, settings.DEFAULT_FROM_EMAIL, [user.email], html_message=html_message)
            return redirect('home')  # Redirect to home page after signup
    else:
        form = GuardianSignupForm()
    return render(request, 'users/guardian_signup.html', {'form': form})



def verify_email(request, token):
    try:
        # Verify and decode the token
        data = signing.loads(token, max_age=settings.EMAIL_VERIFICATION_TOKEN_MAX_AGE)
        user_id = data.get('user_id')
        
        # Get the user and mark their email as verified
        user = User.objects.get(id=user_id)
        user.email_verified = True
        user.save()
        
        messages.success(request, 'Your email has been verified successfully!')
    except (signing.BadSignature, signing.SignatureExpired, User.DoesNotExist):
        messages.error(request, 'Invalid or expired verification link.')
    
    return redirect('home')  # Redirect to the home page