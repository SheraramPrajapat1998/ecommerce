from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin # to show images in admin section
from parler.admin import TranslatableAdmin

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
  list_display = ['name', 'slug']

  def get_prepopulated_fields(self, request, obj=None):
    return {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(AdminImageMixin, TranslatableAdmin):
  list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
  list_filter = ['available', 'created', 'updated']
  list_editable = ['price', 'available']
  
  def get_prepopulated_fields(self, request, obj=None):
    return {'slug': ('name',)}
