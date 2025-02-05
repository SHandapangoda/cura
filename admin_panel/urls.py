from django.urls import path
from . import views

urlpatterns = [
    path('queries/', views.view_queries, name='view_queries'),
    path('queries/<int:query_id>/', views.resolve_query, name='resolve_query'),
    path('queries/update/<int:query_id>/<str:status>/', views.update_query_status, name='update_query_status'),
]