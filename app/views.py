from django.shortcuts import render, redirect
from .models import Customer, Vendor, CustomUser
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomerSignUpForm, VendorSignUpForm

# Create your views here.


def index(request):
    a = CustomUser.objects.all()
    print(a)
    return render(request, 'Signup.html')


def CustomerSignup(request):
    form = CustomerSignUpForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            form = CustomerSignUpForm()
            return render(request, 'login/customerlogin.html', context)
    else:
        form = CustomerSignUpForm()
    return render(request, 'login/customerlogin.html', context)


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


class VendorSignUpView(CreateView):
    model = CustomUser
    form_class = VendorSignUpForm
    template_name = 'signup/vendor_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'vendor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('index')
