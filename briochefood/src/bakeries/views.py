from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status

from bakeries.models import Bakery, Product, Sale

from bakeries.serializer import BakerySerializer, ProductSerializer
from bakeries.validators.recipient_bank_validator import RecipientAndBankSerializer
from bakeries.validators.transaction_validator import TransactionSerializer

from utils.pagarme import Pagarme
from customers.models import Customer
from customers.serializer import CustomerSerializer


class BakeryView(generics.ListCreateAPIView):
    queryset = Bakery.objects.all()
    serializer_class = BakerySerializer


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RecipientAndBankCreateView(APIView):
    def post(self, request, bakery_cnpj):
        try:
            bakery = Bakery.objects.get(cnpj=bakery_cnpj)
        except Bakery.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        serializer = RecipientAndBankSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            Pagarme().create_bank_account(
                serializer.validated_data["bank_account"])

            recipient = Pagarme().create_recipient(serializer.validated_data)

            bakery.update_recipient(recipient["id"])

            return Response({'Recebedor e conta bancária criados!'}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# terminar os testes

class SaleCreateView(APIView):
    def post(self, request, bakery_cnpj):
        try:
            bakery = Bakery.objects.get(cnpj=bakery_cnpj)
        except Bakery.DoesNotExist or not bakery.recipient:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        transaction_serializer = TransactionSerializer(data=request.data)
        transaction_serializer.is_valid(raise_exception=True)

        buy_data = request.data

        try:
            for item in buy_data["items"]:
                product = Product.objects.get(id=item["id"])

                is_available = product.check_stock(item["quantity"])
                if not is_available:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)

                product.update_quantity(quantity_to_buy)

            transaction = Pagarme().create_transaction(buy_data, bakery.recipient)

            customer = Customer.objects.get(
                id=buy_data["customer"]["external_id"])

            sale = Sale(
                transaction=transaction["id"],
                bakery=bakery,
                customer=customer
            )

            sale.save()

            return Response({'Compra realizada!'}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
