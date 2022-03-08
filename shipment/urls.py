from .views import Shipment 

from django.urls import path

urlpatterns = [
    path('api/shipment', Shipment.as_view(), name='shipment'),
]