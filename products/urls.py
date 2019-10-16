from django.conf.urls import url, include
from .views import all_products
from django.urls import path
from . import views


urlpatterns = [
    url(r'products/$', all_products, name='products'),
]