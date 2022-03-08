from django.db.models import fields
from rest_framework import serializers
from shipment.models import Ship

class ShipSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Ship
        fields = "__all__"
    