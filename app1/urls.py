from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('<int:key>/', views.ProductView.as_view(), name="products"),
    path('verify/', views.Verify, name='verify'),
    path('vendor/', views.vendor_add_products, name='vendor'),
    path('<int:key>/product<int:pkey>/cart/', views.cart, name="cart"),
    path('<int:key>/product<int:pkey>/', views.Sprod, name="Sproduct")
]
