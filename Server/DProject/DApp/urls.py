from django.urls import path
from .views import get_member
from .views import create_member

urlspatterns = [
    path('members/', get_member, name='get_member'),
    path('members/create/', create_member, name='create_member'),
]