from django.contrib import admin
from .models import Product
from .models import ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'desc', 'price', 'sale', 'saleToday', 'slug')
    list_editable = ('price', 'saleToday', 'sale')
    prepopulated_fields = {'slug': ('brand','model')}
    inlines = [ ProductImageInline, ] 

admin.site.register(Product, ProductAdmin)