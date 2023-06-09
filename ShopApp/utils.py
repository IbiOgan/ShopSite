import json
from .models import *
# from faker import Faker
# from faker.providers import lorem


def productDetail(request, id):
    product = Product.objects.get(id=id)
    # fake = Faker()
    # for _ in range(5):
    #     print(fake.paragraph(nb_sentences=5, variable_nb_sentences=False))
    # print(fake.sentence())
    description = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Maecenas porttitor congue massa. Fusce posuere, magna sed pulvinar ultricies, purus lectus malesuada libero, sit amet commodo magna eros quis urna. Nunc viverra imperdiet enim. Fusce est. Vivamus a tellus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
Proin pharetra nonummy pede. Mauris et orci. Aenean nec lorem. In porttitor. Donec laoreet nonummy augue. Suspendisse dui purus, scelerisque at, vulputate vitae, pretium mattis, nunc. Mauris eget neque at sem venenatis eleifend.
"""
    return {'product': product, 'description': description}


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    # print('Cart:', cart)
    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0}
    cartItems = order['get_cart_items']
    for i in cart:
        # Try block to prevent error when items are removed
        try:
            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])
            cartItems += cart[i]['quantity']
            order['get_cart_total'] += total
            order['get_cart_items'] = cartItems

            item = {
                'id': product.id,
                'product': {
                    'id': product.id,
                    'product_id': product.product_id,
                    'product_name': product.product_name,
                    'price': product.price,
                },
                'quantity': cart[i]['quantity'],
                'get_total': total,
            }
            items.append(item)
        except:
            print("Item was removed from cart")

    return {'cartItems': cartItems, 'order': order, 'items': items}


def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer_ref=customer,
                                                     complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        cookieData = cookieCart(request)

        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
    return {'cartItems': cartItems, 'order': order, 'items': items}


def guestOrder(request, data):
    print('User is not logged in')
    # print('COOKIES:', request.COOKIES)
    name = data['form']['name']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']

    customer, created = Customer.objects.get_or_create(
        customer_id=email,
    )
    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer_ref=customer,
        complete=False,
    )

    for item in items:
        product = Product.objects.get(id=item['product']['id'])
        orderItem = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity'],
        )

    return customer, order
