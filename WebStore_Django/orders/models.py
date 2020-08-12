from django.db import models
from products.models import Product


# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Статус {0}".format(self.name)

    class Meta:
        verbose_name = "Статус заказа"
        verbose_name_plural = "Статусы заказа"


class Order(models.Model):
    total_order_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ {0} {1}".format(self.id, self.status.name)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    num = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "{0}".format(self.product.name)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"