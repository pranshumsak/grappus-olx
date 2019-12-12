from django.db import models
from .product_models import Product
from .user_models import User
from .b_models import Base


class Favourite(Base):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
