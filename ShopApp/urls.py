from django.urls import path
from ShopApp import views
# from . import views # This is also correct

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product, name='product'),
    path('customer/', views.customer, name='customer'),
    path('order/', views.order, name='order'),
    path('store/', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout')
]
