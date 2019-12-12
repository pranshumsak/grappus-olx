from django import views
from api.models.product_models import Product as myproducts
from django.shortcuts import render
from django.http import HttpResponse


def get_products(request):
    obj = myproducts.objects.filter(is_available=True, is_active=True)
    context = {
        'obj': obj
    }
    return render(request, 'Products.html', context)
