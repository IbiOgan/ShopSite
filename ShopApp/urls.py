from django.urls import path
from ShopApp import views
# from . import views # This is also correct

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register, name='register'),
    path('product/', views.product, name='product'),
    path('product_detail/<product_id>/',
         views.product_detail, name='product_detail'),
    path('order_detail/<order_id>/', views.order_detail, name='order_detail'),
    path('profile/', views.profile, name='profile'),
    path('customer/', views.customer, name='customer'),
    path('order/', views.order, name='order'),
    path('store/', views.store, name='store'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order')
]
