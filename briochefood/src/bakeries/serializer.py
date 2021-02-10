from rest_framework import serializers
from bakeries.models import Bakery, Product, Sale


class BakerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bakery
        fields = '__all__'

    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)
