from django.conf import settings
from .rules_pagarme import *

import pagarme


class FakePagarmeProvider:
    def create_bank_account(self, bank_account):
        return {
            "object": "bank_account",
            "id": 17365090,
            "bank_code": "341",
            "agencia": "0932",
            "agencia_dv": "5",
            "conta": "58054",
            "conta_dv": "1",
            "type": "conta_corrente",
            "document_type": "cpf",
            "document_number": "26268738888",
            "legal_name": "API BANK ACCOUNT",
            "charge_transfer_fees": True,
            "date_created": "2017-01-06T18:52:22.215Z"
        }

    def create_recipient(self, recipient):
        return {
            "object": "recipient",
            "id": "re_cixm61j7e00doin6de8ocgttb",
            "transfer_enabled": True,
            "last_transfer": None,
            "transfer_interval": "weekly",
            "transfer_day": 5,
            "automatic_anticipation_enabled": True,
            "automatic_anticipation_type": "full",
            "automatic_anticipation_days": None,
            "automatic_anticipation_1025_delay": 0,
            "anticipatable_volume_percentage": 85,
            "date_created": "2017-01-06T18:59:35.936Z",
            "date_updated": "2017-01-06T18:59:35.936Z",
            "postback_url": "https://requestb.in/tl0092tl",
            "status": "active",
            "status_reason": None,
            "bank_account": {
                "object": "bank_account",
                "id": 17365090,
                "bank_code": "341",
                "agencia": "0932",
                "agencia_dv": "5",
                "conta": "58054",
                "conta_dv": "1",
                "type": "conta_corrente",
                "document_type": "cpf",
                "document_number": "26268738888",
                "legal_name": "API BANK ACCOUNT",
                "charge_transfer_fees": True,
                "date_created": "2017-01-06T18:52:22.215Z"
            },
            "register_information": {
                "type": "individual",
                "document_number": "92545278157",
                "name": "Someone",
                "site_url": "http://www.site.com",
                "email": "some@email.com",
                "phone_numbers": [{
                    "ddd": "11",
                    "number": "11987654321",
                    "type": "mobile"
                }]
            }
        }

    def set_split_rules(self, recipient_id):
        bakery_split_rule["recipient_id"] = recipient_id
        our_split_rule["recipient_id"] = "re_cixm61j7e00doin6de8ocgttb"

        return [
            bakery_split_rule,
            our_split_rule
        ]

    def create_transaction(self, transaction, recipient_id):
        return {
            "object": "transaction",
            "status": "paid",
            "refse_reason": None,
            "status_reason": "acquirer",
            "acquirer_response_code": "0000",
            "acquirer_name": "pagarme",
            "acquirer_id": "5969170917bce0470c8bf099",
            "authorization_code": "65208",
            "soft_descriptor": None,
            "tid": 1830855,
            "nsu": 1830855,
            "date_created": "2017-08-14T20:35:46.046Z",
            "date_updated": "2017-08-14T20:35:46.455Z",
            "amount": 10000,
            "authorized_amount": 10000,
            "paid_amount": 10000,
            "refunded_amount": 0,
            "installments": 1,
            "id": 1830855,
            "cost": 50,
            "card_holder_name": "Morpheus Fishburne",
            "card_last_digits": "1111",
            "card_first_digits": "411111",
            "card_brand": "visa",
            "card_pin_mode": None,
            "postback_url": None,
            "payment_method": "credit_card",
            "capture_method": "ecommerce",
            "antifraud_score": None,
            "boleto_url": None,
            "boleto_barcode": None,
            "boleto_expiration_date": None,
            "referer": "api_key",
            "ip": "10.2.11.17",
            "subscription_id": None,
            "phone": None,
            "address": None,
            "customer": {
                "object": "customer",
                "id": "2fefb2bf-7182-4346-b49c-7de349cbd9c6",
                "external_id": "#3311",
                "type": "individual",
                "country": "br",
                "document_number": None,
                "document_type": "cpf",
                "name": "Morpheus Fishburne",
                "email": "mopheus@nabucodonozor.com",
                "phone_numbers": [
                    "+5511999998888",
                    "+5511888889999"
                ],
                "born_at": None,
                "birthday": "1965-01-01",
                "gender": None,
                "date_created": "2017-08-14T20:35:45.963Z",
                "documents": [
                    {
                        "object": "document",
                        "id": "doc_cj6cmcm2l01z5696dyamemdnf",
                        "type": "cpf",
                        "number": "30621143049"
                    }
                ]
            },
            "billing": {
                "address": {
                    "object": "address",
                    "street": "Rua Matrix",
                    "complementary": None,
                    "street_number": "9999",
                    "neighborhood": "Rio Cotia",
                    "city": "Cotia",
                    "state": "sp",
                    "zipcode": "06714360",
                    "country": "br",
                    "id": 145818
                },
                "object": "billing",
                "id": 30,
                "name": "Trinity Moss"
            },
            "shipping": {
                "address": {
                    "object": "address",
                    "street": "Rua Matrix",
                    "complementary": None,
                    "street_number": "9999",
                    "neighborhood": "Rio Cotia",
                    "city": "Cotia",
                    "state": "sp",
                    "zipcode": "06714360",
                    "country": "br",
                    "id": 145819
                },
                "object": "shipping",
                "id": 25,
                "name": "Neo Reeves",
                "fee": 1000,
                "delivery_date": "2000-12-21",
                "expedited": True
            },
            "items": [
                {
                    "object": "item",
                    "id": "r123",
                    "title": "Red pill",
                    "unit_price": 10000,
                    "quantity": 1,
                    "category": None,
                    "tangible": True,
                    "venue": None,
                    "date": None
                },
                {
                    "object": "item",
                    "id": "b123",
                    "title": "Blue pill",
                    "unit_price": 10000,
                    "quantity": 1,
                    "category": None,
                    "tangible": True,
                    "venue": None,
                    "date": None
                }
            ],
            "card": {
                "object": "card",
                "id": "card_cj6cmcm4301z6696dt3wypskk",
                "date_created": "2017-08-14T20:35:46.036Z",
                "date_updated": "2017-08-14T20:35:46.524Z",
                "brand": "visa",
                "holder_name": "Morpheus Fishburne",
                "first_digits": "411111",
                "last_digits": "1111",
                "country": "UNITED STATES",
                "fingerprint": "3ace8040fba3f5c3a0690ea7964ea87d97123437",
                "valid": True,
                "expiration_date": "0922"
            },
            "split_rules": None,
            "metadata": {},
            "antifraud_metadata": {},
            "reference_key": None
        }
