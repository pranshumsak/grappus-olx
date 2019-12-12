
from django.urls import path, include
from api.views import product_view

urlpatterns = [
    path('product/', product_view.get_products, name='all_products')
]