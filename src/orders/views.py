from django.shortcuts import render
from cart.cart import Cart

from .models import OrderItem
from .forms import OrderCreateForm

def order_create(request):
  cart = Cart(request)
  form = OrderCreateForm()
  if request.method == 'POST':
    form = OrderCreateForm(data=request.POST)
    if form.is_valid():
      order = form.save()
      for item in cart:
        OrderItem.objects.create(order=order,
          product=item['product'],
          price=item['price'],
          quantity=item['quantity']
        )
        # clear the cart
        cart.clear()
        return render(request, 'orders/order/created.html', {'order':order})
  return render(request, 'orders/order/create.html', {'cart':cart, 'form':form})