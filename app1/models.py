from django.db import models
from django.utils.timezone import datetime

# Create your models here.


class User_details(models.Model):
    fullname = models.CharField(default="kc", max_length=200)
    email = models.EmailField(default="kc@")
    phone = models.CharField(default="123", max_length=10)
    address = models.CharField(default="36 apn", max_length=200)

    def __str__(self):
        return str(self.id) + " " + self.fullname


# class Products(models.Model):

#     product_name = models.CharField(max_length=80)
#     product_price = models.DecimalField(max_digits=7, decimal_places=2)
#     description = models.TextField()

#     def get_product_by_id(ids):

#         return Products.objects.get(ids=id)

#     def get_all_products():

#         return Products.objects.all()

#     def __str__(self):
#         return str(self.product_name)


# class Customer(models.Model):
#     user_name = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=10)
#     email = models.EmailField()
#     address = models.TextField()

#     def register(self):
#         self.save()

#     def get_customer_by_email(email):
#         return Customer.objects.get(email=email)


# class OrderItem(models.Model):
#     # order_id
#     item = models.ForeignKey(Products, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)

#     def ordered_item(product_id):
#         return Products.objects.filter(item=product_id)


# Options = (('0', 'Order Recieved'), ('1', 'order released'),
#            ('2', 'Order dispatched'))


# class Orders(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     order_items = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
#     amount = models.IntegerField()
#     date = models.DateField(default=datetime.today)
#     status = models.CharField(
#         max_length=2, choices=Options, default=None, blank=True)

#     def placeOrder(self):
#         self.save()

#     def get_orders_by_customer(customer_id):
#         return Orders.objects.filter(customer=customer_id).order_by('-date')
