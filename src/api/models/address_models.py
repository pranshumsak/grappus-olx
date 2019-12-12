from . import user_models
from . import b_models
from django.db import models
"""
    Addresses Model contain multiple addresses of users 
"""

class Address(b_models.Base):
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    address = models.TextField()
    landmark = models.CharField(max_length=40)
    zip = models.CharField(max_length=10)
