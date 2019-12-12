from django.db import models
# Create your models here.
"""
    Base model contain common fields which is inherited by all models    
"""


class Base(models.Model):
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

