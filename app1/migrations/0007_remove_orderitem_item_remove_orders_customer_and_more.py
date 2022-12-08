# Generated by Django 4.1.3 on 2022-12-08 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_customer_orderitem_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='item',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='order_items',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]