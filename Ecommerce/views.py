import json
from django.shortcuts import render, redirect
from app.models import slider, baner_area, Main_Category, Product, Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Min, Max, Sum
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from cart.cart import Cart
import requests
from django.db.models import Q


def base(request):
    return render(request, 'index.html')


def home(request):
    obj = slider.objects.all().order_by('-id')[0:3]
    baner = baner_area.objects.all().order_by('-id')[0:3]
    main_category = Main_Category.objects.all().order_by('id')
    product = Product.objects.filter(section__name="TOP DEAL OF THE DAY")
    product1 = Product.objects.filter(section__name="TOP SELL")
    context = {
        'obj': obj,
        'baner': baner,
        'main_category': main_category,
        'product': product,
        'product1': product1,
    }
    print(product)

    return render(request, 'main/home.html', context)


def Product_Details(request, slug):
    product = Product.objects.filter(slug=slug)
    if product.exists:
        product = Product.objects.get(slug=slug)
    else:
        return redirect('error')

    context = {
        'product': product
    }

    return render(request, 'product/product_detail.html', context)


def ProductFilter(request, slug):
    original_string = deslugify(slug)
    product = Product.objects.filter(
        Q(main_category__category__subcategory__name=slug) |
        Q(main_category__category__name=slug) |
        Q(main_category__name=slug)
    )
    context = {
        'product': product,
    }
    return render(request, 'product/product.html', context)


def ERROR(request):
    return render(request, 'error/404error.html')


def MyAccount(request):
    if (request.method == 'POST'):
        name = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User(
            username=name, first_name=firstname, last_name=lastname, email=email)
        user.set_password(password)
        user.save()
        messages.success(request, 'Register sucessfully')

    return render(request, 'login/customerlogin.html')


@login_required(login_url='/vendor/customer_signup')
def update(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id

        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        user.save()
        return redirect('login')
    return render(request, 'login/customer_update_page.html')


def custom_logout(request):
    logout(request)
    return redirect('home')


def ABOUT(request):
    return render(request, 'main/about.html')


def CONTACT(request):
    return render(request, 'main/contact.html')


def PRODUCT(request):
    category = Category.objects.all()
    product = Product.objects.all()
    context = {
        'category': category,
        'product': product,
    }
    return render(request, 'product/product.html', context)


def ProductFilter(request):
    category = Category.objects.all()
    product = Product.objects.all()
    context = {
        'category': category,
        'product': product,
    }
    return render(request, 'product/product.html', context)


def filter_data(request):
    categories = request.GET.getlist('category[]')
    brands = request.GET.getlist('brand[]')
    print("this is categor")
    print(categories)
    allProducts = Product.objects.all().order_by('-id').distinct()
    if len(categories) > 0:
        allProducts = allProducts.filter(
            Categories__id__in=categories).distinct()

    if len(brands) > 0:
        allProducts = allProducts.filter(Brand__id__in=brands).distinct()

    t = render_to_string('ajax/product_list.html', {'product': allProducts})
    print(t)

    return JsonResponse({'data': t})


@login_required(login_url='/vendor/customer_signup')
def CART(request):
    cart = request.session.get('cart')
    print(cart)
    # it's new for me
    packing_cost = sum(i['packing_cost'] for i in cart.values()
                       if i and i.get('packing_cost') is not None)
    tax = sum(i['tax'] for i in cart.values()
              if i and i.get('packing_cost') is not None)
    context = {
        'packing_cost': packing_cost,
        'tax': tax,
    }

    return render(request, 'cart/cart.html', context)

# cart functionality added


@login_required(login_url='/app/customer_signup')
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url='/app/my_account')
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url='/app/customer_signup')
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url='/app/customer_signup')
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url='/app/customer_signup')
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url='/app/customer_signup')
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')


@login_required(login_url='/app/customer_signup')
def Checkout(request):
    cart = request.session.get('cart')

    cart_items = []

    if cart:
        for item_id, item_data in cart.items():
            item_name = item_data['product_name']
            item_price = item_data['price']
            item_quantity = item_data['quantity']
            cart_items.append({
                'id': item_id,
                'name': item_name,
                'price': item_price,
                'quantity': item_quantity,
            })

    context = {
        'cart_items': cart_items
    }
    print(context)

    return render(request, 'checkout/checkout.html', context)


def verify_payment(request):
    print(request.POST)
    token = request.POST.get('payload[token]')
    amount = request.POST.get('payload[amount]')
    # product_id = data['product_identity']
    # token = data['token']
    # amount = data['amount']
    url = "https://khalti.com/api/v2/payment/verify/"

    payload = {
        'token': token,
        'amount': amount
    }

    headers = {
        'Authorization': 'Key test_secret_key_0ebe9337a9924683b75ba7b679cbd18f'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    response_data = json.loads(response.text)
    status_code = str(response.status_code)

    if status_code == '4000':
        response = JsonResponse(
            {'status': 'false', 'message': response_data['detail']}, status=500)
        return response
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(response_data)
    return JsonResponse(f"Payment Done !! With IDX.{response_data['user']['idx']}", safe=False)
