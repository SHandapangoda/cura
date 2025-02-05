from django.shortcuts import get_object_or_404, redirect
from .models import Query
from django.core.mail import send_mail

def update_query_status(request, query_id, status):
    query = get_object_or_404(Query, id=query_id)
    query.status = status
    query.save()
    
    # Send email notification
    send_mail(
        'Your Query Status Updated',
        f'Your query "{query.subject}" is now marked as {status}.',
        'admin@cura.com',
        [query.user.email],
    )
    
    return redirect('view_queries')
