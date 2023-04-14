from django.urls import path
from ShopApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product, name='product'),
]
