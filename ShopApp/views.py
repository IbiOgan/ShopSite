from .utils import cookieCart, cartData, guestOrder, productDetail
from .models import *
import json
from django.http import JsonResponse
import datetime
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):
    data = cartData(request)
    cartItems = data['cartItems']
    context = {
        'cartItems': cartItems
    }

    if request.user.is_authenticated:
        return redirect('store')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('store')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return redirect('index')
    else:
        return render(request, 'ShopApp/index.html', context)


def logout_page(request):
    logout(request)
    return redirect('index')
    # Redirect to a success page.


def register(request):
    data = cartData(request)
    cartItems = data['cartItems']
    context = {
        'cartItems': cartItems
    }
    if request.user.is_authenticated:
        return redirect('store')

    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data.get('password1')
    #         email = form.cleaned_data['email']
    #         user = authenticate(username=username, password=password)
    #         login(request, user)
    #         messages.success(
    #             request, "Your account has been successfully created.")
    #         return redirect('store')
    # else:
    #     form = UserCreationForm()

    # context = {
    #     'cartItems': cartItems,
    #     'form': form
    # }
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password1)
                user.is_active = True
                user.save()
                user = authenticate(username=username, password=password1)
                login(request, user)
                messages.success(request, "Registration successful.")
                return redirect('index')
        else:
            messages.info(request, 'Password not matching..')
            return redirect('register')
        # return redirect('/')

    return render(request, 'ShopApp/register.html', context)


@login_required(login_url='index')
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


@login_required(login_url='index')
def dashboard(request):
    data = cartData(request)
    cartItems = data['cartItems']
    products = Product.objects.all().count()
    orders = Order.objects.all().count()
    customers = Customer.objects.all().count()
    staffs = User.objects.filter(is_staff=True).count()*400
    print(products, orders, customers, staffs)
    context = {
        'cartItems': cartItems,
        'products': products,
        'orders': orders,
        'customers': customers,
        'staffs': staffs,
    }
    if not (request.user.is_superuser):
        return redirect('store')
    return render(request, 'ShopApp/dashboard.html', context)


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


@login_required(login_url='index')
def order_detail(request, order_id):
    orderItems = OrderItem.objects.filter(order=order_id)
    data = cartData(request)
    cartItems = data['cartItems']
    context = {
        'cartItems': cartItems,
        'order_id': order_id,
        'orderItems': orderItems,
    }
    return render(request, 'ShopApp/order_detail.html', context)


@login_required(login_url='index')
def profile(request):
    # product_details = productDetail(request, product_id)
    # product = product_details['product']
    # description = product_details['description']
    customer = request.user.customer
    orders = Order.objects.filter(
        customer_ref=customer, complete=True).order_by('-date_ordered')
    # for order in orders:
    #     print(order)
    #     print(order.orderitem_set.all())
    # orderItems = OrderItem.objects.filter(order_ref=orders)
    data = cartData(request)
    cartItems = data['cartItems']
    context = {
        'cartItems': cartItems,
        'orders': orders,
    }
    return render(request, 'ShopApp/profile.html', context)


@login_required(login_url='index')
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


@login_required(login_url='index')
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
