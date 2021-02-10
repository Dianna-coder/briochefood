from rest_framework import serializers


class BankSerializer(serializers.Serializer):
    agencia = serializers.IntegerField()
    agencia_dv = serializers.IntegerField()
    bank_code = serializers.IntegerField()
    conta = serializers.IntegerField()
    conta_dv = serializers.IntegerField()
    document_number = serializers.IntegerField()
    legal_name = serializers.CharField(max_length=100)


class RecipientAndBankSerializer(serializers.Serializer):
    transfer_day = serializers.IntegerField()
    transfer_interval = serializers.CharField(max_length=10)
    bank_account = BankSerializer()
