from rest_framework import serializers

from .models import CreditOrder, Contract, Manufacturer, Product


class CreditOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditOrder
        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
