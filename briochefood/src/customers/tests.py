from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from customers import models


class TestCustomerCreateView(APITestCase):
    def test_post_WHEN_requested_with_valid_inputs_THEN_creates_a_customer(self):
        customer_data = {
            "name": "Bread Dinner",
            "email": "bread.dinner@email.com",
            "cpf": "00756475082",
            "phone_number": "11985717689",
            "birthday": "1999-01-01",
            "country": "BR",
            "state": "SP",
            "city": "Guarulhos",
            "neighborhood": "bread",
            "street": "Avenue Bread",
            "street_number": 2,
            "zipcode": "078239485"
        }

        url_create_customer = reverse('get_and_create_customer')

        response = self.client.post(
            url_create_customer, customer_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Customer.objects.all().count(), 1)
