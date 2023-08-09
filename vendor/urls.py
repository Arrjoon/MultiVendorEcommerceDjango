from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='vendor_home'),
    path('product/', views.product, name='vendor_product'),
    path('addproduct/', views.Add_product, name='vendor_addproduct'),
    path('check_slug/', views.check_slug, name='check_slug'),
    path('vendor_login/', views.vendor_login, name='vendor_login'),
]
