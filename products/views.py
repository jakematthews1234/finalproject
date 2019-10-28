from django.shortcuts import render
from .models import Product

# A view that shows all Products within the DB
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})