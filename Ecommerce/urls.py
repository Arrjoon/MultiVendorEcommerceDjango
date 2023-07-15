"""Ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('about/', views.ABOUT, name='about'),
    path('contact/', views.CONTACT, name='contact'),
    path('product/', views.PRODUCT, name='product'),
    path('product/<slug:slug>', views.Product_Details, name='product_detail'),
    path('404', views.ERROR, name='error'),
    path('account/Register', views.MyAccount, name='account'),
    path('account/login', views.Login, name='login'),
    path('update_account', views.update, name='update'),
    path('logout', views.custom_logout, name='logout'),
    path('product/filter/filter_data', views.filter_data, name="filter-data"),
    path('cart/', views.CART, name='cart_detail'),
    path('checkout/', views.Checkout, name='checkout'),

    # cart functionality added
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),

    path('vendor/', include('vendor.urls')),

] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
