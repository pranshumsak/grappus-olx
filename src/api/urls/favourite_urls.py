from django.urls import path
from api.views import favourite_views

urlpatterns = [
    path('favourite/<int:id>', favourite_views.favourite)
]