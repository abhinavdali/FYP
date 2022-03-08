from django.shortcuts import render
from .serializer import ShipSerializer
from .models import Ship
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import generics, permissions

# Create your views here.
class Shipment(generics.GenericAPIView):
    serializer_class = Ship
    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = ShipSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    def get(self, request, *args, **kwargs):
        posts = Ship.objects.all()
        serializer = ShipSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)