from django.conf.urls import url, include
from .views import testimonials

urlpatterns = [
    url(r'^testimonials/$', testimonials, name='testimonials'),

]