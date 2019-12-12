from django.urls import path
from api.views import order_view

urlpatterns = [
    path('product/cart/order/', order_view.order)
]