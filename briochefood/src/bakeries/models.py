import uuid
from django.db import models

from customers.models import Customer


class Bakery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cnpj = models.CharField(max_length=14)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    recipient = models.CharField(max_length=28, null=True)

    class Meta:
        verbose_name = "Bakery"
        verbose_name_plural = "Bakeries"
        db_table = 'bakeries'

    def __str__(self):
        return f'{self.name}'

    def update_recipient(self, recipient_id):
        self.recipient = recipient_id
        self.save()


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    unit_price = models.CharField(max_length=20)
    quantity = models.IntegerField()
    bakery = models.ForeignKey(
        Bakery, related_name='product_bakery_fk', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = 'products'

    def __str__(self):
        return f'{self.title}'

    def check_stock(self, quantity_to_buy):
        is_available = (self.quantity - int(quantity_to_buy)) >= 0
        return is_available

    def update_quantity(self, quantity_to_buy):
        self.quantity = (self.quantity - int(quantity_to_buy))
        self.save()


class Sale(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transaction = models.IntegerField()
    bakery = models.ForeignKey(
        Bakery, related_name='sales_bakery_fk', on_delete=models.CASCADE)
    customer = models.ForeignKey(
        Customer, related_name='sales_customer_fk', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"
        db_table = 'sales'

    def __str__(self):
        return f'{self.id} '
