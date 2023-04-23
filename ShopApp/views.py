from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
import json
from .models import *

# Create your views here.


def index(request):

    return render(request, 'ShopApp/index.html')


def product(request):
    # products = Product.objects.get_queryset().order_by('id')
    products = Product.objects.all().order_by('id')
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page', 1)
    page_list = paginator.page(page_number)
    try:
        page_list = paginator.page(page_number)
    except PageNotAnInteger:
        page_list = paginator.page(1)
    except EmptyPage:
        page_list = paginator.page(paginator.num_pages)
    return render(request, 'ShopApp/product.html', {
        'page_list': page_list,
        'range': range(1, 11)
    })


def customer(request):
    customers = Customer.objects.all().order_by('id')
    paginator = Paginator(customers, 10)
    page_number = request.GET.get('page', 1)
    page_list = paginator.page(page_number)
    try:
        page_list = paginator.page(page_number)
    except PageNotAnInteger:
        page_list = paginator.page(1)
    except EmptyPage:
        page_list = paginator.page(paginator.num_pages)
    return render(request, 'ShopApp/customer.html', {
        'page_list': page_list,
        'range': range(1, 11)
    })


def order(request):
    orders = Order.objects.all().order_by('id')
    paginator = Paginator(orders, 10)
    page_number = request.GET.get('page', 1)
    page_list = paginator.page(page_number)
    try:
        page_list = paginator.page(page_number)
    except PageNotAnInteger:
        page_list = paginator.page(1)
    except EmptyPage:
        page_list = paginator.page(paginator.num_pages)
    return render(request, 'ShopApp/order.html', {
        'page_list': page_list,
        'range': range(1, 11)
    })


def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer_ref=customer,
                                                     complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    products = Product.objects.all().order_by('id')
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page', 1)
    page_list = paginator.page(page_number)
    try:
        page_list = paginator.page(page_number)
    except PageNotAnInteger:
        page_list = paginator.page(1)
    except EmptyPage:
        page_list = paginator.page(paginator.num_pages)
    context = {
        'page_list': page_list,
        'range': range(1, 11),
        'cartItems': cartItems
    }
    return render(request, 'ShopApp/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer_ref=customer,
                                                     complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'order': order, 'items': items}
    return render(request, 'ShopApp/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer_ref=customer,
                                                     complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'order': order, 'items': items}
    return render(request, 'ShopApp/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action', action)
    print('ProductId', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer_ref=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)
