import uuid
from django.db import models


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)
    phone_number = models.CharField(max_length=20)
    birthday = models.DateField()
    country = models.CharField(max_length=2)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=20)
    neighborhood = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    street_number = models.CharField(max_length=10)
    zipcode = models.IntegerField()

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        db_table = 'customers'

    def __str__(self):
        return f'{self.name}'
