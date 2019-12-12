from django.db import models


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length= 50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=60)
    payment_method = models.CharField(max_length=100)
    payment_data = models.CharField(max_length=100)