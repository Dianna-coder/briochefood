from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from utils.pagarme.fake_pagarme import FakePagarmeProvider
from bakeries.use_cases.create_recipient_and_bank_account import *

from bakeries import models


class TestCreateRecipientAndBankAccountUseCase(APITestCase):
    def test_use_case_WHEN_requested_with_valid_fields_THEN_creates_a_recipient_and_bank_to_bakery(self):
        bakery = models.Bakery(
            cnpj='35443081000189',
            name='Yogurt Bakery',
            address='Avenue Bakery',
        )
        bakery.save()

        data = {
            "transfer_day": "5",
            "transfer_interval": "weekly",
            "bank_account": {
                "agencia": "0932",
                "agencia_dv": "5",
                "bank_code": "341",
                "conta": "58054",
                "conta_dv": "1",
                "document_number": "26268738888",
                "legal_name": "HOUSE TARGARYEN"
            }
        }

        pagarme_provider = FakePagarmeProvider()
        CreateRecipientAndBankAccountUseCase(
            pagarme_provider).execute(data, bakery)

        bakery.refresh_from_db()

        self.assertIsNotNone(bakery.recipient)
