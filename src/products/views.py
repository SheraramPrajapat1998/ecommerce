from django.shortcuts import render, get_object_or_404

from .models import Category, Product
from cart.forms import CartAddProductForm

def product_list(request, category_slug=None):
  category = None
  categories = Category.objects.all()
  products = Product.objects.available()

  if category_slug:
    category = get_object_or_404(Category, slug=category_slug)
    products = products.filter(category=category)

  cart_product_form = CartAddProductForm()
  context = {
    'category': category,
    'categories': categories,
    'products': products,
    'cart_product_form': cart_product_form

  }
  return render(request, 'products/list.html', context)

def product_detail(request, slug, id):
  product = get_object_or_404(Product, slug=slug, id=id, available=True)
  cart_product_form = CartAddProductForm()
  context = {
    'product': product,
    'cart_product_form': cart_product_form
  }
  return render(request, 'products/detail.html', context)

