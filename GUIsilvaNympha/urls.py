from django.urls import path, include

urlpatterns = [
    path('', include('pomiary.urls')),
]