from .views import Pricing 

from django.urls import path

urlpatterns = [
    path('api/pricing', Pricing.as_view(), name='pricing'),
]