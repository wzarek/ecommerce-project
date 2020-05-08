from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^product/(?P<slug>[\w-]+)/$', views.singleprod, name='singleprod'),
    re_path(r'^search/$', views.search, name='search'),
    re_path(r'^products/(?P<cat>[\w-]+)/$', views.category, name='category'),
    re_path(r'^products/(?P<cat>[\w-]+)/(?P<subcat>[\w-]+)/$', views.subcategory, name='subcategory'),
    re_path(r'^products/(?P<cat>[\w-]+)/(?P<subcat>[\w-]+)/(?P<slug>[\w-]+)/$', views.subcatprod, name='subcatprod')

]