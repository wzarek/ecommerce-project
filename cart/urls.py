from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.cart, name='cart'),
    re_path(r'^(?P<slug>[\w-]+)/(?P<quantity>\d+)/$', views.updateCart, name='update_cart')
]

