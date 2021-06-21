from rest_framework import serializers
from .models import *


class CustomerSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Customer
        fields = '__all__'


class CsvProductSerializer( serializers.ModelSerializer ):
    customer = CustomerSerializer( many=True )

    class Meta:
        model = CsvProduct
        fields = '__all__'
