# from django.db import models


# class Order(models.Model):
#     ORDER_STATUS_CHOICES = (
#         ('processing', 'Processing'),
#         ('shipped', 'Shipped'),
#         ('delivered', 'Delivered'),
#         ('cancelled', 'Cancelled'),
#     )
#     order_id = models.AutoField(primary_key=True)
#     customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
#     order_date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(
#         max_length=50, choices=ORDER_STATUS_CHOICES, default='Processing')
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)


# class OrderDetail(models.Model):
#     detail_id = models.AutoField(primary_key=True)
#     order = models.ForeignKey(
#         'Order', related_name='order_details', on_delete=models.CASCADE)
#     product = models.ForeignKey('Product', on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     unit_price = models.DecimalField(max_digits=10, decimal_places=2)
#     subtotal = models.DecimalField(max_digits=10, decimal_places=2)
