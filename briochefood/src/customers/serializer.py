from rest_framework import serializers
from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)
