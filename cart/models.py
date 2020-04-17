from django.db import models
from shop.models import Product


class Cart(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return "Cart %s" %(self.id)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
