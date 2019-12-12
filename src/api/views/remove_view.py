from api.models.favourite_models import Favourite
from django.shortcuts import render, redirect
from django.http import HttpResponse
from api.models.product_models import Product


def remove(request, id):
    p = Product.objects.get(pk=id)
    p.delete()
    p.save()
    return redirect('cart_page')