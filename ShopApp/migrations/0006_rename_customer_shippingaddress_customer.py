# Generated by Django 4.2 on 2023-04-24 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0005_remove_customer_email_remove_customer_password_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='Customer',
            new_name='customer',
        ),
    ]
