from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
from django.contrib import messages


def index(request):
    myproducts = Product.objects.all()
    context = {
        'name': 'Oranges',
        'myproducts': myproducts,
    }
    return render(request, "home.html", context)


def product_list(request):
    products_list = Product.objects.all()
    context = {
        'products_list': products_list,
    }
    return render(request, "product_list.html", context)


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Product added successfully.")
                return redirect('product_list')
            except Exception as e:
                messages.error(request, f'Error adding the product: {e}')
        else:
            messages.error(request, "Unable to save the product.")
    else:
        form = ProductForm()
    return render(request, "add_product.html", {'form': form})


def update_product(request, pk):
    instance = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=instance)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Product Updated successfully!')
                return redirect('product_list')
            except Exception as e:
                messages.error(request, f'Error updating product: {e}')
        else:
            messages.error("Unable to to update the product")
    else:
        form = ProductForm(instance=instance)
    return render(request, 'update_product.html', {'form': form})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        try:
            product.delete()
            messages.success(request, 'Product deleted successfully')
            return redirect('product_list')
        except Exception as e:
            messages.error(request, f"Unable to delete the product: {e}")
    return render(request, 'delete_product.html', {'product': product})
