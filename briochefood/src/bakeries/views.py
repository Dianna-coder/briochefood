from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status

from bakeries.models import Bakery, Product

from bakeries.serializer import BakerySerializer, ProductSerializer
from bakeries.validators.recipient_bank_validator import RecipientAndBankSerializer
from bakeries.validators.transaction_validator import TransactionSerializer

from utils.pagarme.pagarme import Pagarme

from bakeries.use_cases.create_recipient_and_bank_account import *
from bakeries.use_cases.create_sale import *


class BakeryView(generics.ListCreateAPIView):
    queryset = Bakery.objects.all()
    serializer_class = BakerySerializer


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RecipientAndBankCreateView(APIView):
    def post(self, request, bakery_cnpj):
        serializer = RecipientAndBankSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            bakery = Bakery.objects.get(cnpj=bakery_cnpj)
        except Bakery.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:
            pagarme_provider = Pagarme()

            CreateRecipientAndBankAccountUseCase(
                pagarme_provider).execute(request.data, bakery)

            return Response({'Recebedor e conta bancária criados!'}, status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SaleCreateView(APIView):
    def post(self, request, bakery_cnpj):
        transaction_serializer = TransactionSerializer(data=request.data)
        transaction_serializer.is_valid(raise_exception=True)

        try:
            bakery = Bakery.objects.get(cnpj=bakery_cnpj)
        except Bakery.DoesNotExist or not bakery.recipient:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:
            buy_data = request.data

            for item in buy_data["items"]:
                product = Product.objects.get(id=item["id"])

                is_available = product.check_stock(item["quantity"])
                if not is_available:
                    return Response({f'O item {product.title} não está disponível para compra!'}, status=status.HTTP_401_UNAUTHORIZED)

                product.update_quantity(item["quantity"])

            pagarme_provider = Pagarme()

            CreateSaleUseCase(pagarme_provider).execute(buy_data, bakery)

            return Response({'Compra realizada!'}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
