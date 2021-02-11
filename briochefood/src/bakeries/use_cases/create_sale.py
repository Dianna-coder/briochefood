from bakeries.models import Sale
from customers.models import Customer


class CreateSaleUseCase:
    def __init__(self, pagarme_provider):
        self.pagarme_provider = pagarme_provider

    def execute(self, buy_data, bakery):
        transaction = self.pagarme_provider.create_transaction(
            buy_data, bakery.recipient)

        customer = Customer.objects.get(
            id=buy_data["customer"]["external_id"])

        sale = Sale(
            transaction=transaction["id"],
            bakery=bakery,
            customer=customer
        )

        sale.save()

        return sale
