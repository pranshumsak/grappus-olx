from api.views import cart_view
from django.urls import path


urlpatterns = [
    path('product/cart/', cart_view.cart, name='cart_page')
]