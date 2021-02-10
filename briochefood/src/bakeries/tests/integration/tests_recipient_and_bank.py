# from rest_framework import status
# from rest_framework.reverse import reverse
# from rest_framework.test import APITestCase

# from unittest.mock import MagicMock

# from bakeries import models

# from utils.pagarme import Pagarme


# class TestRecipientAndBankCreateView(APITestCase):
#     def test_post_WHEN_requested_with_valid_inputs_THEN_creates_a_recipient_and_bank_to_bakery(self):
#         bakery = models.Bakery(
#             cnpj='35443081000189',
#             name='Yogurt Bakery',
#             address='Avenue Bakery',
#         )
#         bakery.save()

#         pagarme = Pagarme()
#         pagarme.create_account = MagicMock(return_value=True)
#         pagarme.create_recipient = MagicMock(return_value=True)

#         request_data = {
#             "transfer_day": "5",
#             "transfer_interval": "weekly",
#             "bank_account": {
#                 "agencia": "0932",
#                 "agencia_dv": "5",
#                 "bank_code": "341",
#                 "conta": "58054",
#                 "conta_dv": "1",
#                 "document_number": "26268738888",
#                 "legal_name": "HOUSE TARGARYEN"
#             }
#         }

#         url_create_recipient_and_bank = reverse(
#             'create_recipient_and_bank',
#             kwargs={'bakery_cnpj': bakery.cnpj}
#         )

#         response = self.client.post(
#             url_create_recipient_and_bank, request_data, format='json')

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         # self.assertEqual(models.Bakery.objects.all().count(), 1)
