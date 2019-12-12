from api.models.favourite_models import Favourite
from django.shortcuts import render


def cart(request):
    fav = Favourite.objects.all()
    price = count_price(fav)
    context = {
        'fav': fav,
        'price': price
    }
    return render(request, 'cart.html', context)


def count_price(c):
    count = 0
    for i in c:
        count += i.product.price
    return count
