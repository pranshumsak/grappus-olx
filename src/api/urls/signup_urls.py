from django.urls import path
from api.views import signup_view

urlpatterns = [
    path('signup/', signup_view.sign_up, name="signup_page")
]