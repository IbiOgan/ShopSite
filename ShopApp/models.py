from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.TextField()
    product_name = models.TextField()
    category = models.TextField()
    brand = models.TextField()
    price = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.id}, {self.product_id}, {self.product_name}, {self.category}, {self.brand}, {self.price}"


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,
                                null=True,
                                blank=True,
                                on_delete=models.CASCADE)
    customer_id = models.TextField(null=True, blank=True)
    email = models.TextField(default="N/A")
    password = models.CharField(max_length=100, default="N/A")

    def __str__(self):
        return f"{self.id}, {self.customer_id}, {self.order_id}, {self.email}"


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    customer_ref = models.ForeignKey(Customer,
                                     null=True,
                                     blank=True,
                                     on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}, {self.customer_ref}, {self.order_id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              blank=True,
                              null=True,
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                blank=True,
                                null=True,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product}, {self.quantity}, {self.date_added}"


class ShippingAddress(models.Model):
    Customer = models.ForeignKey(Customer,
                                 on_delete=models.SET_NULL,
                                 null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
