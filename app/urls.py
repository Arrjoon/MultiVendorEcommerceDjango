from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('customer_signup', CustomerSignup, name='customer_signup'),
    path('vendor_signup', VendorSignUpView.as_view(), name='vendor_signup'),
]
