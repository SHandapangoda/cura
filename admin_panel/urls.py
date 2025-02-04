from django.urls import path
from . import views

urlpatterns = [
    path('queries/', views.view_queries, name='view_queries'),
    path('queries/<int:query_id>/', views.resolve_query, name='resolve_query'),
]