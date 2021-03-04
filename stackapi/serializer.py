from rest_framework import serializers
from .models import Price, Pricesilver


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('__all__')

class PricesilverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricesilver
        fields = ('__all__')
