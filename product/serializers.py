from rest_framework import serializers
from models import Products

class ProductSerializer(serializers):
    class Meta:
        model = Products
        fields = '__all__'
        