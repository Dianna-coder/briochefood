from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from utils.pagarme.fake_pagarme import FakePagarmeProvider
from bakeries.use_cases.create_sale import *

from bakeries import models as bakeries_models
from customers import models as customers_models

from rest_framework import status

transaction_data = {
    "amount": "10000",
    "payment_method": "credit_card",
    "card_number": "4111111111111111",
    "card_cvv": "123",
    "card_expiration_date": "0922",
    "card_holder_name": "Morpheus Fishburne",
    "customer": {
        "external_id": "2fefb2bf-7182-4346-b49c-7de349cbd9c6",
        "name": "Arroz de teste",
        "type": "individual",
        "country": "br",
        "email": "mopheus@nabucodonozor.com",
        "documents": [
            {
                "type": "cpf",
                "number": "30621143049"
            }
        ],
        "phone_numbers": ["+5511999998888", "+5511888889999"],
        "birthday": "1965-01-01"
    },
    "billing": {
        "name": "Trinity Moss",
        "address": {
            "country": "br",
            "state": "sp",
            "city": "Cotia",
            "neighborhood": "Rio Cotia",
            "street": "Rua Matrix",
            "street_number": "9999",
            "zipcode": "06714360"
        }
    },
    "shipping": {
        "name": "Arroz de teste",
        "fee": "1000",
        "delivery_date": "2000-12-21",
        "expedited": True,
        "address": {
            "country": "br",
            "state": "sp",
            "city": "Cotia",
            "neighborhood": "Rio Cotia",
            "street": "Rua Matrix",
            "street_number": "9999",
            "zipcode": "06714360"
        }
    },
    "items": [
        {
            "id": "9dd2b3cf-9e1b-4927-9cd7-24aa85a61a83",
            "title": "Red pill",
            "unit_price": "10000",
            "quantity": "1",
            "tangible": True
        }
    ]
}


class TestCreateSaleUseCase(APITestCase):
    def test_use_case_WHEN_requested_with_valid_fields_THEN_creates_a_bakery_sale(self):
        bakery = bakeries_models.Bakery(
            cnpj='35443081000189',
            name='Yogurt Bakery',
            address='Avenue Bakery',
        )
        bakery.save()

        product = bakeries_models.Product(
            id='9dd2b3cf-9e1b-4927-9cd7-24aa85a61a83',
            title='Red pill',
            unit_price=10000,
            quantity=10,
            bakery=bakery
        )

        product.save()

        customer = customers_models.Customer(
            id='2fefb2bf-7182-4346-b49c-7de349cbd9c6',
            name='Bread Dinner',
            email='bread.dinner@email.com',
            cpf='00756475082',
            phone_number='11985717689',
            birthday='1999-01-01',
            country='BR',
            state='SP',
            city='Guarulhos',
            neighborhood='bread',
            street='Avenue Bread',
            street_number=2,
            zipcode='078239485'
        )
        customer.save()

        pagarme_provider = FakePagarmeProvider()
        sale = CreateSaleUseCase(pagarme_provider).execute(
            transaction_data, bakery)

        self.assertIsNotNone(bakeries_models.Sale.objects.get(id=sale.id))
