from django.db import models
from .user_models import User


class Buyers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
