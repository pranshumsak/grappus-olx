from django.shortcuts import render
from django import http
from api.models.seller_models import Seller
from django.contrib.auth import authenticate, login

def to_base(request):
    ob = Seller.objects.get(user=request.user)
    context = {ob}
    return render(request, 'base.html', context)

