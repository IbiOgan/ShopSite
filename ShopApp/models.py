from django.db import models
from django.contrib.auth.models import User, auth
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    # id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,
                                null=True,
                                blank=True,
                                on_delete=models.CASCADE)
    customer_id = models.TextField(null=True, blank=True)
    # email = models.TextField(default="N/A")
    # password = models.CharField(max_length=100, default="N/A")

    def __str__(self):
        return f"{self.customer_id}"
        # return f"{self.id}, {self.customer_id}, {self.order_id}, {self.email}"


@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance, customer_id=instance.username)


@receiver(post_save, sender=User)
def save_customer(sender, instance, **kwargs):
    instance.customer.save()


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    customer_ref = models.ForeignKey(Customer,
                                     null=True,
                                     blank=True,
                                     on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

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

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return f"{self.product}, {self.quantity}, {self.date_added}"


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,
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
