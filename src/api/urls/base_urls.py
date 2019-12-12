
from django.urls import path, include
from . import product_urls
from . import signup_urls
from . import login_urls
from . import favourite_urls
from . import cart_urls
from . import order_urls
from . import remove_urls
from . import welcome_urls
from . import purchased_urls
from api.views.base_views import to_base


urlpatterns = [
    path('', to_base, name="base_page"),
    path('', include(product_urls)),
    path('', include(signup_urls)),
    path('', include(login_urls)),
    path('', include(favourite_urls)),
    path('', include(cart_urls)),
    path('', include(order_urls)),
    path('', include(remove_urls)),
    path('', include(welcome_urls)),
    path('', include(purchased_urls)),
]

