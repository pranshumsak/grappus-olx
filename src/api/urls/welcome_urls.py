from django.urls import path
from api.views import welcome_view

urlpatterns = [
    path('', welcome_view.welcome, name='welcome_page')
]