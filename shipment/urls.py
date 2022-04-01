from .views import Shipment, ShipmentView 

from django.urls import path

urlpatterns = [
    path('api/shipment', Shipment.as_view(), name='shipment'),
    path('api/shipmentView', ShipmentView.as_view(), name='shipment_view'),
]