from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from bakeries import models


class TestProductView(APITestCase):
    def test_get_WHEN_all_products_are_requested_THEN_return_all(self):
        bakery = models.Bakery(
            cnpj='35443081000189',
            name='Yogurt Bakery',
            address='Avenue Bakery'
        )
        bakery.save()

        product = models.Product(
            title='Bread Test',
            unit_price='10000',
            quantity=1000,
            bakery=bakery
        )
        product.save()

        url_get_and_create_product = reverse('get_and_create_product')

        response = self.client.get(url_get_and_create_product)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], product.title)

    def test_post_WHEN_requested_with_INVALID_inputs_THEN_returns_400(self):
        product_data = {
            "title": "Bread"
        }

        url_get_and_create_product = reverse('get_and_create_product')

        response = self.client.post(
            url_get_and_create_product, product_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_WHEN_requested_with_valid_inputs_THEN_creates_a_product(self):
        bakery = models.Bakery(
            cnpj='35443081000189',
            name='Yogurt Bakery',
            address='Avenue Bakery',
        )
        bakery.save()

        product_data = {
            "title": "Bread Test",
            "unit_price": "10000",
            "quantity": 1000,
            "bakery": bakery.id
        }

        url_get_and_create_product = reverse('get_and_create_product')

        response = self.client.post(
            url_get_and_create_product, product_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Bakery.objects.all().count(), 1)
