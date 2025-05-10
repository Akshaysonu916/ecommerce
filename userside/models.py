from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
        def __str__(self):
                return self.username

class Products(models.Model):
        product_name=models.CharField(max_length=100)
        description=models.CharField(max_length=100,blank=True)
        price=models.IntegerField()
        image=models.ImageField(upload_to='images')


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.product.price * self.quantity