from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('customer_signup', CustomerSignup, name='customer_signup'),
    path('vendor_signup', VendorSignUp, name='vendor_signup'),
    path('vendor_login', Vendor_Login, name='vendorlogin'),
    path('login', Login, name='login'),
]
