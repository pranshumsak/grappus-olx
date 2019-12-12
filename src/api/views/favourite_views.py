from api.models.favourite_models import Favourite
from django.shortcuts import render
from api.models.product_models import Product
from django.http import HttpResponse


def favourite(request, id):
    p = Product.objects.get(pk=id)
    try:
        try:
            fav = Favourite.objects.get(product=p)
            return HttpResponse("Product is already added in cart")
        except:
            f = Favourite(product=p, user=request.user)
            f.save()
            context = {'f': f}
            return render(request, "favourite.html", context)
    except:
        pass
