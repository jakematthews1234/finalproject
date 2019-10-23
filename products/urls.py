from django.conf.urls import url, include
from .views import all_products
from . import views


urlpatterns = [
    url(r'', all_products, name='products'),
    url(r'products/$', all_products, name='products'),
]