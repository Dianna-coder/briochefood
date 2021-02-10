from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from bakeries import models


class TestBakeryView(APITestCase):
    def test_post_WHEN_requested_with_valid_inputs_THEN_creates_a_bakery(self):
        bakery_data = {
            "cnpj": "35443081000189",
            "name": "Yogurt Bakery",
            "address": "Avenue Bakery",
        }

        url_create_bakery = reverse('get_and_create_bakery')

        response = self.client.post(
            url_create_bakery, bakery_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            models.Bakery.objects.get(cnpj=bakery_data["cnpj"]).cnpj,
            bakery_data["cnpj"]
        )
