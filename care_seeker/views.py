from django.shortcuts import render
from care_provider.models import CareProvider

def find_care_provider(request):
    available_providers = CareProvider.objects.filter(is_available=True)
    
    # Apply filters based on care seeker's preferences
    if request.GET.get('task'):
        available_providers = available_providers.filter(tasks__contains=request.GET.get('task'))
    
    return render(request, 'care_seeker/find_care_provider.html', {'providers': available_providers})
