from rest_framework import serializers
from shipment.models import Ship

class ShipSerializer(serializers.ModelSerializer):   
    user = serializers.ReadOnlyField(source='user.user')

    class Meta:
        model = Ship
        fields = ("user", "username", "of_type", "weight", "size", "price")













