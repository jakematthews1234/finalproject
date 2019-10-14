from django.conf.urls import url, include
from .views import all_products
from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome, name="welcome"),
    url(r'^$', all_products, name='products'),
]