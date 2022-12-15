from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # Default url for auth
    path('', include('django.contrib.auth.urls')),
    # Page for registrations
    path('register/', views.register, name='register')
]
