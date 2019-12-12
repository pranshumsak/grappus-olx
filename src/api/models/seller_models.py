from . import user_models
from django.db import models
""" 
    This model contain specific details of seller and inherits users model
"""


class Seller(models.Model):
    user = models.OneToOneField(user_models.User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
