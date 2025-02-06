from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  # Add this line
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/care-seeker/', views.care_seeker_signup, name='care_seeker_signup'),
    path('signup/care-provider/', views.care_provider_signup, name='care_provider_signup'),
    path('signup/guardian/', views.guardian_signup, name='guardian_signup'),
    path('dashboard/care-seeker/', views.care_seeker_dashboard, name='care_seeker_dashboard'),
    path('dashboard/care-provider/', views.care_provider_dashboard, name='care_provider_dashboard'),
    path('dashboard/guardian/', views.guardian_dashboard, name='guardian_dashboard'),
    path('verify-email/<str:token>/', views.verify_email, name='verify_email'),
    path('landing/', views.landing_page, name='landing_page'),

    # Password reset URLs
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html',
        email_template_name='users/password_reset_email.html',
        subject_template_name='users/password_reset_subject.txt'
    ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'
    ), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'
    ), name='password_reset_complete'),
]