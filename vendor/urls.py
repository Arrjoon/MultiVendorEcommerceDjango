from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='vendor_home'),
    path('product/', views.product, name='vendor_product'),
    path('addproduct/', views.Add_product, name='vendor_addproduct'),
    path('check-vendor-name/', views.check_vendor_name, name='check_vendor_name'),
]
