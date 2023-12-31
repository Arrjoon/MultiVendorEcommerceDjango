from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)


class Vendor(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class slider(models.Model):
    DISCOUNT_DEAL = (
        ('hot deals', 'HOT DEAlS'),
        ('new Arrivals', 'New Arraival'),
    )

    Image = models.ImageField(upload_to='images')
    Discount_Deal = models.CharField(choices=DISCOUNT_DEAL, max_length=100)
    Sale = models.IntegerField()
    Brand_Name = models.CharField(max_length=200)
    Discount = models.IntegerField()
    Link = models.CharField(max_length=200)

    def __str__(self):
        return self.Brand_Name


class baner_area(models.Model):
    image = models.ImageField(upload_to='banner_image')
    Discount_Deal = models.CharField(max_length=100)
    Quote = models.CharField(max_length=100)
    Discount = models.IntegerField()

    def __str__(self):
        return self.Quote


class Main_Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    main_category = models.ForeignKey(Main_Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.main_category.name + "--" + self.name


class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.category.main_category.name + "--" + self.category.name + "--"+self.name


class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    vendor_name = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    total_quantity = models.IntegerField()
    Availability = models.IntegerField(null=True)
    featured_image = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    Discount = models.IntegerField()
    tax = models.IntegerField(null=True)
    packing_cost = models.IntegerField(null=True)
    Product_Information = RichTextField(null=True)
    model_name = models.CharField(max_length=100, null=True)
    Categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    Tags = models.CharField(max_length=100, null=True)
    Description = RichTextField(blank=True)
    section = models.ForeignKey(
        Section, on_delete=models.DO_NOTHING, blank=True)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("product_detail", kwargs={'slug': self.slug})

    class Meta:
        db_table = "app_Product"


def create_slug(instance, new_slug=None):
    slug = slugify(instance.product_name)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, Product)


class Product_image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200)


class Additional_Information(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.CharField(max_length=100)
    detail = RichTextField()


class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )
    order_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50, choices=ORDER_STATUS_CHOICES, default='Processing')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)


class OrderDetail(models.Model):
    detail_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(
        'Order', related_name='order_details', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
