from django.shortcuts import render, get_object_or_404

from .models import Category, Product

def product_list(request, category_slug=None):
  category = None
  categories = Category.objects.all()
  products = Product.objects.available()

  if category_slug:
    category = get_object_or_404(Category, slug=category_slug)
    products = products.filter(category=category)
  context = {
    'category': category,
    'categories': categories,
    'products': products
  }
  return render(request, 'products/list.html', context)

def product_detail(request, slug, id):
  product = get_object_or_404(Product, slug=slug, id=id, available=True)
  context = {
    'product': product
  }
  return render(request, 'products/detail.html', context)

