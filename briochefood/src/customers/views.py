from rest_framework import generics
from customers.models import Customer
from customers.serializer import CustomerSerializer


class CustomerView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
