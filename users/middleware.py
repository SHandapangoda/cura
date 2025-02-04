from django.shortcuts import redirect
from django.urls import reverse

class RoleBasedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of URLs to exclude from redirection
        excluded_urls = [
            reverse('login'),  # Exclude login page
            reverse('signup'),  # Exclude signup page
            reverse('verify_email', args=['token']),  # Exclude email verification page
            reverse('password_reset'),  # Exclude password reset page
            reverse('password_reset_done'),  # Exclude password reset done page
            reverse('password_reset_confirm', args=['uidb64', 'token']),  # Exclude password reset confirm page
            reverse('password_reset_complete'),  # Exclude password reset complete page
        ]

        # Check if the current URL is in the excluded list
        if request.path_info in excluded_urls:
            return self.get_response(request)

        # Redirect unauthenticated users to the login page
        if not request.user.is_authenticated:
            return redirect('login')

        # Continue with the request
        response = self.get_response(request)
        return response