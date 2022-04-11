from .views import Shipment, ShipmentUpdate, ShipmentView 

from django.urls import path

urlpatterns = [
    path('api/shipment', Shipment.as_view(), name='shipment'),
    path('api/shipmentView', ShipmentView.as_view(), name='shipment_view'),
    path('api/shipmentUpdate/<tracking>', ShipmentUpdate.as_view(), name='shipment_view'),
]