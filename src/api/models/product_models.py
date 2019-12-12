from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
from .user_models import User
from .b_models import Base


class Categories(Base):
    category_name = models.CharField(max_length=20, blank=False, null=False)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)


class Product(Base):
    product_name = models.CharField(max_length=20, null=False, blank=False, verbose_name="Product Name")
    price = models.BigIntegerField(blank=False, null=False)
    product_desc = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(null=True, blank=True)
    specifications = ArrayField(models.CharField(max_length=200), blank=False)
    is_available = models.BooleanField(default=False)
