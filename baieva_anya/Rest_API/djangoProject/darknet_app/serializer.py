from rest_framework import serializers
from .models import Products


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'url', 'name', 'price', 'amount', 'company')
