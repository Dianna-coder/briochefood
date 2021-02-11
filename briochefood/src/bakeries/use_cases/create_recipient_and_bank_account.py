class CreateRecipientAndBankAccountUseCase:
    def __init__(self, pagarme_provider):
        self.pagarme_provider = pagarme_provider

    def execute(self, data, bakery):
        bank_account = self.pagarme_provider.create_bank_account(
            data["bank_account"])
        recipient = self.pagarme_provider.create_recipient(data)

        bakery.update_recipient(recipient["id"])
