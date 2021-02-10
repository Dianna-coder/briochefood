from rest_framework import serializers


class DocumentSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=10)
    number = serializers.IntegerField()


class CustomerSerializer(serializers.Serializer):
    external_id = serializers.UUIDField()
    name = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=10)
    country = serializers.CharField(max_length=2)
    email = serializers.EmailField()
    documents = serializers.ListField(child=DocumentSerializer())
    phone_numbers = serializers.ListField()
    birthday = serializers.DateField()


class AddressSerializer(serializers.Serializer):
    country = serializers.CharField(max_length=10)
    state = serializers.CharField(max_length=10)
    city = serializers.CharField(max_length=10)
    neighborhood = serializers.CharField(max_length=100)
    street = serializers.CharField(max_length=10)
    street_number = serializers.CharField(max_length=10)
    zipcode = serializers.IntegerField()


class ShippingSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    fee = serializers.IntegerField()
    delivery_date = serializers.DateField()
    expedited = serializers.BooleanField()
    address = AddressSerializer()


class BillingSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    address = AddressSerializer()


class ItemSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField(max_length=100)
    unit_price = serializers.IntegerField()
    tangible = serializers.BooleanField()
    quantity = serializers.IntegerField()


class TransactionSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    payment_method = serializers.CharField(max_length=100)
    customer = CustomerSerializer()
    shipping = ShippingSerializer()
    billing = BillingSerializer()
    items = serializers.ListField(child=ItemSerializer())
