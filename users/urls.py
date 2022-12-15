from django.urls import path, include


app_name = 'users'
urlpatterns = [
    # Default url for auth
    path('', include('django.contrib.auth.urls'))
]
