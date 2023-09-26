from django.http import JsonResponse
from django.shortcuts import render
from app.models import Category, Product
from .forms import Add_Product_Form

# Create your views here.


def profile(request):
    return render(request, 'vendor/home.html')


def product(request):
    category = Category.objects.all()
    product = Product.objects.filter(vendor_name='sugam').values()
    context = {
        'category': category,
        'product': product,
    }
    return render(request, 'vendor/product.html', context)


def Add_product(request):
    if request.method == 'POST':
        form = Add_Product_Form(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            form = Add_Product_Form()
            # Redirect or do something else on successful form submission
    else:
        form = Add_Product_Form()

    context = {
        'form': form
    }
    return render(request, 'vendor/addproduct.html', context)


def check_slug(request):
    slug = request.GET.get('Slug', None)
    response_data = {
        'exists': Product.objects.filter(slug=slug).exists()
    }
    return JsonResponse(response_data)


def vendor_login(request):
    return render(request, 'vendor/vendor_registerform.html')
