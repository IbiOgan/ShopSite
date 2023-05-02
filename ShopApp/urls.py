from django.urls import path
from ShopApp import views
# from . import views # This is also correct

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product, name='product'),
    path('product_detail/<product_id>/',
         views.product_detail, name='product_detail'),
    path('customer/', views.customer, name='customer'),
    path('order/', views.order, name='order'),
    path('store/', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order')
]
