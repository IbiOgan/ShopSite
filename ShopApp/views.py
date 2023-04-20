from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Customer, Order

# Create your views here.


def index(request):

    return render(request, 'ShopApp/index.html')


def product(request):
    products = Product.objects.all()
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
    customers = Customer.objects.all()
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
    orders = Order.objects.all()
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
    context = {}
    return render(request, 'ShopApp/store.html', context)


def cart(request):
    context = {}
    return render(request, 'ShopApp/cart.html', {'range': range(1, 21)})


def checkout(request):
    context = {}
    return render(request, 'ShopApp/checkout.html', context)