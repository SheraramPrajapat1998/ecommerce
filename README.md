# ecommerce


### 1.  products
    - Category
    - Product

### 2.  cart
    - cart functionality(add or remove product and cart detail)
    - cart available to all templates (context_processors)
  
### 3.  orders
    - Order
    - OrderItem
    **Admin site functionality**    - order detail
                                    - export to CSV
                                    - pdf view

### 4.  coupons
    - Coupon
    **coupon functionality**    - cart
                                - order
                                - admin section(in order detail, pdf view)


**Internationalisation**
    site is available in *English, Hindi and Spanish*.




Notes:
###### Windows Erros and links to solve 
    - CommandError: Can't find msguniq. Make sure you have GNU gettext tools 0.15 or newer installed.
    https://stackoverflow.com/questions/33841832/cant-find-msguniq-django-1-8-windows-7-64-bit