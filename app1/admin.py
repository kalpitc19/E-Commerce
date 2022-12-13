from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(User_details)
admin.site.register(Products)
admin.site.register(OrderItem)
admin.site.register(Order)
