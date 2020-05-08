from django.contrib import admin
from .models import Product
from .models import ProductImage
from .models import ProductCategory
from .models import ProductSize

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

class ProductSizeInline(admin.TabularInline):
    model = ProductSize

class ProductAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'desc', 'price', 'sale', 'saleToday', 'slug')
    list_editable = ('price', 'saleToday', 'sale')
    prepopulated_fields = {'slug': ('brand','model')}
    inlines = [ ProductImageInline, ProductSizeInline] 

class CatAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug' : ('title',)}

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, CatAdmin)
admin.site.register(ProductSize)