from django.shortcuts import render, redirect
from .models import Customer, Vendor, CustomUser
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomerSignUpForm, VendorSignUpForm
from django.contrib.auth import authenticate

# Create your views here.


def index(request):
    a = CustomUser.objects.all()
    print(a)
    return render(request, 'Signup.html')


def CustomerSignup(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Account created successfully. You can now log in.')
            form = CustomerSignUpForm()
            return render(request, 'login/customerlogin.html', {'form': form})
    else:
        form = CustomerSignUpForm()

    return render(request, 'login/customerlogin.html', {'form': form})


def Login(request):
    if (request.method == 'POST'):
        name = request.POST.get('username')
        password = request.POST.get('password')
        print(name)
        print(password)
        user = authenticate(request, username=name, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "User name and password not valid")

    return render(request, 'login/customerlogin.html')


# class CustomerSignUpView(CreateView):
#     model = CustomUser
#     form_class = CustomerSignUpForm
#     template_name = 'login/customerlogin1.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'customer'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)


# class VendorSignUpView(CreateView):
#     model = CustomUser
#     form_class = VendorSignUpForm
#     template_name = 'signup/vendor_signup.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'vendor'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         # login(self.request, user)
#         return redirect('index')
def VendorSignUp(request):
    if request.method == 'POST':
        form = VendorSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Account created successfully. You can now log in.')
            form = VendorSignUpForm()
            return redirect('vendorlogin')
    else:
        form = VendorSignUpForm()

    return render(request, 'vendor/vendor_register1.html', {'form': form})


# def Vendor_Login(request):
#     is_vendor = False
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         print(user)
#         if user.is_authenticated:
#             is_vendor = request.user.is_vendor
#             print(is_vendor)
#         print(is_vendor)
#         if user is not None and is_vendor:
#             login(request, user)
#             # Redirect to the vendor dashboard or any other vendor-specific page
#             return redirect('vendor_home')
#         else:
#             print("Error occurs")
#             messages.error(request, 'Invalid login credentials for vendor.')

#     return render(request, 'vendor/vendor_login.html')
def Vendor_Login(request):
    is_vendor = False

    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        print(name)
        print(password)
        user = authenticate(request, username=name, password=password)
        print(user)

        if user is not None:
            # Check if 'is_vendor' attribute exists before accessing it
            if hasattr(user, 'is_vendor') and user.is_vendor:
                is_vendor = True
                login(request, user)
                # Redirect to the vendor dashboard or any other vendor-specific page
                return redirect('vendor_home')
            else:
                messages.error(request, 'User is not a vendor.')
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'vendor/vendor_login.html')
