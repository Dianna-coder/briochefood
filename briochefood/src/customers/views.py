from rest_framework import generics
from customers.models import Customer
from customers.serializer import CustomerSerializer

# adicionar comentário
#
#
#
class CustomerView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

#
#
#
#