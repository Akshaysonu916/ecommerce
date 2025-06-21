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

class Order(models.Model):
    PAYMENT_CHOICES = [
        ('cod', 'Cash on Delivery'),
        ('bank', 'Bank Transfer'),
    ]
    
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    address = models.TextField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.product.product_name} by {self.customer_name}"


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.product.price * self.quantity
    

class Review(models.Model):
    product = models.ForeignKey(Products, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5 stars
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review by {self.user} on {self.product.product_name}"