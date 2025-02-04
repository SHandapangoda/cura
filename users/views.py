from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import User
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Send verification email
            subject = 'Verify Your Email Address'
            html_message = render_to_string('users/verification_email.html', {'user': user})
            plain_message = strip_tags(html_message)
            send_mail(subject, plain_message, settings.DEFAULT_FROM_EMAIL, [user.email], html_message=html_message)
            return redirect('login')  # Redirect to login page after signup
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})

def home(request):
    return render(request, 'users/home.html') 


def verify_email(request, token):
    user_id = verify_verification_token(token)
    if user_id:
        user = User.objects.get(id=user_id)
        user.email_verified = True
        user.save()
        messages.success(request, 'Your email has been verified!')
    else:
        messages.error(request, 'Invalid or expired verification link.')
    return redirect('home')

def landing_page(request):
    return render(request, 'users/landing_page.html')