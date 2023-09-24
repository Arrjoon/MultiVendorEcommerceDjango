from django.contrib import admin
from .models import *
# Register your models here.


class Product_Images(admin.TabularInline):
    model = Product_image


class Additional_Informations(admin.TabularInline):
    model = Additional_Information


class Product_Admin(admin.ModelAdmin):
    inlines = (Product_Images, Additional_Informations)
    list_display = ['product_name', 'price', 'Categories', 'section']
    list_editable = ['Categories', 'section']


class Order_Admin(admin.ModelAdmin):
    list_display = ['order_date', 'customer_id', 'status', 'total_amount']
    list_editable = ['customer_id', 'status']


admin.site.register(CustomUser)
admin.site.register(Vendor)
admin.site.register(Customer)
admin.site.register(Section)
admin.site.register(Product, Product_Admin)
admin.site.register(Product_image)
admin.site.register(Additional_Information)

admin.site.register(slider)
admin.site.register(baner_area)
admin.site.register(Main_Category)
admin.site.register(Category)
admin.site.register(Sub_Category)

admin.site.register(Order, Order_Admin)
admin.site.register(OrderDetail)
