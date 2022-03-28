from .serializer import ShipSerializer
from .models import Ship
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import generics, permissions
import uuid
# Create your views here.
class Shipment(generics.GenericAPIView):
    queryset = Ship.objects.all()
    serializer_class = Ship
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        tracking = uuid.uuid4()
        data = JSONParser().parse(request)
        serializer = ShipSerializer(data = data)
        if serializer.is_valid():
            serializer.save(user=request.user, tracking_number = tracking)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    def get(self, request, *args, **kwargs):
        posts = Ship.objects.all()
        serializer = ShipSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
