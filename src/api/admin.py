from django.contrib import admin
from .models import user_models
from .models import product_models
from .models import buyer_models
from .models import seller_models
from .models import favourite_models

# Register your models here.

admin.site.register(user_models.User)
admin.site.register(product_models.Product)
admin.site.register(buyer_models.Buyers)
admin.site.register(seller_models.Seller)
admin.site.register(favourite_models.Favourite)

