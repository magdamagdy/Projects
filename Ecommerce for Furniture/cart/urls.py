from django.urls import path
from . import views
from django.conf.urls import url

from .views import add_to_cart, add_quantity,  remove_cart

urlpatterns = [
    path('cart_items/',views.show_items , name='show_items'),
    path('offers/',views.offers , name='offers'),
    path('checkout/',views.checkout , name='checkout'),
    path('confirm/',views.confirm , name='confirm'),
    url(r'^add_to_cart/(?P<pk>\d+)$', add_to_cart, name='add_to_cart'),
    url(r'^add_quantity/(?P<pk>\d+)$', add_quantity, name='add_quantity'),
    url(r'^remove_cart/(?P<pk>\d+)$', remove_cart, name='remove_cart'),

]
