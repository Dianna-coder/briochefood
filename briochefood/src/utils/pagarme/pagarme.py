from django.conf import settings
from .rules_pagarme import *

import pagarme


class Pagarme:
    def __init__(self):
        self.our_api_key = settings.PAGARME_CHAVE_API
        self.our_recipient_id = settings.PAGARME_RECIPIENT_ID

        pagarme.authentication_key(self.our_api_key)

    def create_bank_account(self, bank_account):
        return pagarme.bank_account.create(bank_account)

    def create_recipient(self, recipient):
        return pagarme.recipient.create({**recipient_rule, **recipient})

    def set_split_rules(self, recipient_id):
        bakery_split_rule["recipient_id"] = recipient_id
        our_split_rule["recipient_id"] = self.our_recipient_id

        return [
            bakery_split_rule,
            our_split_rule
        ]

    def create_transaction(self, transaction, recipient_id):
        if recipient_id:
            transaction["split_rules"] = self.set_split_rules(recipient_id)

        return pagarme.transaction.create(transaction)
