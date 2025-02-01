from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('care-seeker/signup/', views.care_seeker_signup, name='care_seeker_signup'),
]