import datetime
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
import json
from .models import *
from .utils import cookieCart, cartData, guestOrder, productDetail

# Create your views here.


def index(request):
    data = cartData(request)
    cartItems = data['cartItems']
    context = {
        'cartItems': cartItems
    }
    return render(request, 'ShopApp/index.html', context)


def product(request):
    data = cartData(request)
    cartItems = data['cartItems']

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

    context = {
        'page_list': page_list,
        'range': range(1, 11),
        'cartItems': cartItems
    }
    return render(request, 'ShopApp/product.html', context)


def product_detail(request, product_id):
    product_details = productDetail(request, product_id)
    product = product_details['product']
    description = product_details['description']
    data = cartData(request)
    cartItems = data['cartItems']
    context = {
        'cartItems': cartItems,
        'product': product,
        'description': description,
    }
    return render(request, 'ShopApp/product_detail.html', context)


def customer(request):
    data = cartData(request)
    cartItems = data['cartItems']

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

    context = {
        'page_list': page_list,
        'range': range(1, 11),
        'cartItems': cartItems
    }
    return render(request, 'ShopApp/customer.html', context)


def order(request):
    data = cartData(request)
    cartItems = data['cartItems']

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

    context = {
        'page_list': page_list,
        'range': range(1, 11),
        'cartItems': cartItems
    }
    return render(request, 'ShopApp/order.html', context)


def store(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all().order_by('id')
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page', 1)
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


def search(request):
    data = cartData(request)
    cartItems = data['cartItems']
    search_brand = request.GET.get('brand', request.GET.get('brand1'))
    search_word = request.GET.get('searchWord', request.GET.get('searchWord1'))
    if search_brand == "All Brands":
        products = Product.objects.filter(
            product_name__contains=search_word).order_by('id')
    else:
        products = Product.objects.filter(
            brand=search_brand).filter(product_name__contains=search_word).order_by('id')
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page', 1)
    if paginator.num_pages > 10:
        page_range = 11
    else:
        page_range = paginator.num_pages + 1
    try:
        page_list = paginator.page(page_number)
    except PageNotAnInteger:
        page_list = paginator.page(1)
    except EmptyPage:
        page_list = paginator.page(paginator.num_pages)
    context = {
        'page_list': page_list,
        'range': range(1, page_range),
        'cartItems': cartItems,
        'brand1': search_brand,
        'searchWord1': search_word
    }
    return render(request, 'ShopApp/store.html', context)


def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'order': order, 'items': items, 'cartItems': cartItems}
    return render(request, 'ShopApp/cart.html', context)


def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'order': order, 'items': items, 'cartItems': cartItems}
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
    else:
        orderItem.quantity = 0

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse(f'Item was {action}ed', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer_ref=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.order_id = str(transaction_id)

    if total == float(order.get_cart_total):
        order.complete = True
    order.save()

    ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],
    )

    return JsonResponse('Payment submitted..', safe=False)
