from django.urls import path, include
from users.views import home

urlpatterns = [
    path('', home, name='home'),
    path('users/', include('users.urls')),  # Include users app URLs
]