from django.db import models

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
    customer_id = models.TextField()
    email = models.TextField(default="N/A")
    password = models.CharField(max_length=100, default="N/A")

    def __str__(self):
        return f"{self.id}, {self.customer_id}, {self.order_id}, {self.email}"


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.TextField()
    customer_ref = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}, {self.customer_ref}, {self.order_id}"
