import csv
import os
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError

from django.contrib.auth.models import User
from ShopApp.models import Product, Customer, Order


class Command(BaseCommand):
    help = 'Import data from csv file'

    def handle(self, *args, **options):

        # drop all data from tables
        User.objects.all().delete()
        Product.objects.all().delete()
        Customer.objects.all().delete()
        Order.objects.all().delete()
        # create table again

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/ShopApp/data/kzElectronicStore.csv', newline='') as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)  # skip the header line
            for row in reader:
                if len(row) < 8:
                    next(reader)
                else:
                    print(row)
                    list = row[4].split(".")
                    name = list[len(list) - 1]
                    product = Product.objects.create(
                        product_id=row[2],
                        category=row[4],
                        brand=row[5],
                        price=float(row[6]),
                        product_name=row[5] + " " + name,
                    )
                    product.save()

                    # User.objects.filter(username=row[7]).exists() also works
                    if not (User.objects.filter(username=row[7]).first()):

                        user = User.objects.create_user(username=row[7],
                                                        email='N/A',
                                                        password='12345')
                        user.is_active = True
                        user.save()

                        # shabby way to synch customer and user. instead use post_save signal
                        # customer = Customer.objects.create(
                        #     user=user,
                        #     customer_id=row[7],
                        # )
                        # customer.save()

                    order = Order.objects.create(
                        order_id=row[2],
                        customer_ref=Customer.objects.filter(
                            customer_id=row[7]).first(),
                    )
                    order.save()
