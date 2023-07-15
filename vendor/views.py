from django.http import JsonResponse
from django.shortcuts import render
from app.models import Category, Product
from .forms import Add_Product_Form

# Create your views here.


def profile(request):
    return render(request, 'vendor/home.html')


def product(request):
    category = Category.objects.all()
    product = Product.objects.filter(vendor_name='Arjun').values()
    context = {
        'category': category,
        'product': product,
    }
    return render(request, 'vendor/product.html', context)


def Add_product(request):
    if request.method == 'POST':
        form = Add_Product_Form(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or do something else on successful form submission
    else:
        form = Add_Product_Form()

    context = {
        'form': form
    }
    return render(request, 'vendor/addproduct.html', context)


def check_vendor_name(request):
    vendor_name = request.GET.get('vendor_name', None)
    response_data = {
        'exists': Product.objects.filter(vendor_name=vendor_name).exists()
    }
    return JsonResponse(response_data)
