from django.urls import path
from . import views


urlpatterns = [
    path('book/', views.book_care_provider, name='book_care_provider'),
    path('track/<int:booking_id>/', views.track_booking, name='track_booking'),
    path('find-care-provider/', views.find_care_provider, name='find_care_provider'),

]