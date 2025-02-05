from django.urls import path, include
from users.views import home  # Import the home view from users.views

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('users/', include('users.urls')),  # Include other user-related URLs
]