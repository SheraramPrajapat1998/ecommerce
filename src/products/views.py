from django.shortcuts import render, get_object_or_404

from .models import Category, Product
from cart.forms import CartAddProductForm

def product_list(request, category_slug=None):
  category = None
  categories = Category.objects.all()
  products = Product.objects.filter(available=True)

  language = request.LANGUAGE_CODE
  if category_slug:
    category = get_object_or_404(Category, translations__language_code=language, translations__slug=category_slug)
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
  language = request.LANGUAGE_CODE
  product = get_object_or_404(Product, translations__language_code=language, translations__slug=slug, available=True)
  print(product)
  cart_product_form = CartAddProductForm()
  context = {
    'product': product,
    'cart_product_form': cart_product_form
  }
  return render(request, 'products/detail.html', context)

