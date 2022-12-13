from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.template import loader
from django.utils import timezone

# Create your views here."


def index(request):
    if (request.method == "POST"):
        add = User_details()
        add.fullname = request.POST.get('fullname')
        add.email = request.POST.get('email')
        add.phone = request.POST.get('phone')
        add.address = request.POST.get('address')
        add.save()
        # detail = User_details.objects.get()
        # obj = User_details.objects.filter(testfield=12).order_by('-id')[0]
        obj = User_details.objects.last()
        return redirect("products", key=obj.id)

    return render(request, "app1/index.html")


# def product_list(request):
#     return render(request, "app1/productionList.html")


class ProductView(ListView):
    template_name = "app1/productList.html"
    context_object_name = 'productsList'

    def get_queryset(self):
        return Products.get_all_products()


def Verify(request):
    if (request.method == "POST"):
        name = request.POST.get('fullname')
        if User_details.objects.get(fullname=name):
            obj = User_details.objects.get(fullname=name)
            return redirect("products", key=obj.id)
    return render(request, "app1/verification.html")


def vendor_add_products(request):

    if request.method == "POST":
        if request.POST.get('product_name') and request.POST.get('product_price'):
            product = Products()
            product.product_name = request.POST.get('product_name')
            product.product_price = request.POST.get('product_price')
            product.description = request.POST.get('description', "")
            product.save()

    return render(request, 'app1/vendor.html')


def cart(request, key, pkey):
    list = OrderItem()
    if (request.method == "POST"):
        add = OrderItem()
        prod = Products.objects.get(pk=pkey)
        add.item_name = prod.product_name
        add.quantity = request.POST.get('quantity')
        add.save()
    items = OrderItem.objects.get(
        item_name=Products.objects.get(id=pkey))
    context = {
        'orderList': items
    }
    return render(request, 'app1/cart.html', context)


def Sprod(request, key, pkey):
    if (request.method == "POST"):
        item = request.POST.get('quantity')
        add = OrderItem()
        add.item_name = Products.objects.get(pk=pkey)
        add.quantity = item
        add.save
    prod = Products.objects.get(pk=pkey)
    context = {
        'product': prod
    }
    return render(request, 'app1/Sproduct.html', context)
