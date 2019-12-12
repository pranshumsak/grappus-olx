from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here1.
"""
    Users model contain all user details even of seller and buyers
"""
GenderChoices = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others')
)


class User(AbstractUser):
    contact_no = models.CharField(max_length=14)
    gender = models.CharField(choices=GenderChoices, max_length=1)
    dob = models.DateField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="static/images")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(blank=True, null=True)
