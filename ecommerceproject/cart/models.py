from django.db import models
from ecommerceapp.models import Product 
# Create your models here.

class Cart(models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    date=models.DateField(auto_now_add=True)
    class Meta:
        db_table='Cart'
        ordering=['date']
    
    def __str__(self):
        return self.cart_id
    
class Cartitem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    class Meta:
        db_table='CartItem'
    def subtotal(self):
        return self.quantity * self.product.price
    def __str__(self):
        return self.product