from django.urls import path
from api.views import remove_view

urlpatterns = [
    path('product/cart/remove/<int:id>', remove_view.remove, name='remove_page')
]