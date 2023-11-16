from django.shortcuts import render
from django.http import HttpResponse
from . models import Product


def index(request):
    myproducts = Product.objects.all()
    context = {
        'name': 'Oranges',
        'myproducts': myproducts,
    }
    return render(request, "hello_django.html", context)
