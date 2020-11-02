from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from products.models import Product
from coupons.forms import CouponApplyForm

from .cart import Cart
from .forms import CartAddProductForm

@require_POST
def cart_add(request, product_id):
  cart = Cart(request)
  product = get_object_or_404(Product, id=product_id)
  form = CartAddProductForm(data=request.POST)
  if form.is_valid():
    cd = form.cleaned_data
    cart.add(product, quantity=cd['quantity'], override_quantity=cd['override'])
  return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
  cart = Cart(request)
  product = get_object_or_404(Product, id=product_id)
  cart.remove(product)
  return redirect('cart:cart_detail')

def cart_detail(request):
  cart = Cart(request)
  for item in cart:
    item['update_quantity_form'] = CartAddProductForm(initial={
      'quantity': item['quantity'],
      'override': True
    })
  coupon_apply_form = CouponApplyForm()  
  context = {
    'cart':cart,
    'coupon_apply_form': coupon_apply_form
  }
  return render(request, 'cart/detail.html', context)
