from django.urls import path
from api.views import submit_view

urlpatterns = [
    path('product/cart/order/purchased/', submit_view.purchased, name='purchased_page')
]
