from django.db import models
from django.utils.timezone import datetime

# Create your models here.


class User_details(models.Model):
    fullname = models.CharField(default="", max_length=200)
    email = models.EmailField(default="")
    phone = models.CharField(default="", max_length=10)
    address = models.CharField(default="", max_length=200)

    def __str__(self):
        # return str(self.id) + " " + self.fullname
        return str(self.id) + " " + str(self.fullname)


class Products(models.Model):
    product_name = models.CharField(max_length=80)
    product_price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()

    def get_product_by_id(ids):

        return Products.objects.get(ids=id)

    def get_all_products():

        return Products.objects.all()

    def __str__(self):
        # return str(self.product_name) + "    " + str(self.product_price)
        return str(self.product_name)


class OrderItem(models.Model):
    # order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, default="")
    item_name = models.ForeignKey(
        Products, on_delete=models.CASCADE, default="", null=True)
    quantity = models.IntegerField(default=0)

    def ordered_item(item_name):
        return Products.objects.filter(item=item_name)

    def __str__(self):
        # return str(self.product_name) + "    " + str(self.product_price)
        return str(self.item_name) + " " + str(self.quantity)

    def get_all_products():
        return OrderItem.objects.all()


class Order(models.Model):
    customer = models.ForeignKey(
        User_details, on_delete=models.CASCADE, null=True, default="")
    orders = models.ForeignKey(
        OrderItem, on_delete=models.CASCADE, default="", null=True)
    Amount = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return str(self.orders)
