from django.db import models
from sorl.thumbnail import ImageField
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields

class Category(TranslatableModel):
  translations = TranslatedFields(
    name  = models.CharField(max_length=200, db_index=True),
    slug  = models.SlugField(max_length=200, unique=True),
  )
  class Meta:
  #   # ordering = ('name', )
    verbose_name = 'category'
    verbose_name_plural = 'categories'

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('products:product_list_by_category', args=[self.slug])

# class ProductManager(models.Manager):
#   def available(self):
#     return Product.objects.filter(available=True)

class Product(TranslatableModel):
  translations = TranslatedFields(
    name          = models.CharField(max_length=200, db_index=True),
    slug          = models.SlugField(max_length=200, db_index=True),
    description   = models.TextField(blank=True),
  )
  category      = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
  image         = ImageField(upload_to='products/%Y/%m/%d', blank=True, default='no_image.jpg')
  price         = models.DecimalField(max_digits=10, decimal_places=2)
  available     = models.BooleanField(default=True)
  created       = models.DateTimeField(auto_now_add=True)
  updated       = models.DateTimeField(auto_now=True)

  # objects       = ProductManager()

  # class Meta:
  #   ordering = ('name', )
  #   index_together = (('id', 'slug'), )

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('products:product_detail', args=[self.id, self.slug])
