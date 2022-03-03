from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, viewsets
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth.models import User
from .serializers import UserSerializer, RegisterSerializer

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

# MIN_LENGTH = 8

# class UserSerializer(serializers.ModelSerializer):

#     password = serializers.CharField(
#         write_only = True,
#         min_length = MIN_LENGTH,
#         error_messages = {
#             "min_length":"Password must be longer than {MIN_LENGTH} characters."
#         }
#     )

#     password2 = serializers.CharField(
#         write_only = True,
#         min_length = MIN_LENGTH,
#         error_messages = {
#             "min_length":"Password must be longer than {MIN_LENGTH} characters."
#         }
#     )

#     class Meta:
#         model = User
#         fields = "__all__"
    
#     def validate(self, data):
#         if data["password"] != data["password2"]:
#             raise serializers.ValidationError("Password does not match.")
#         return data

#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data["username"],
#             email =validated_data["email"],
#             first_name = validated_data["first_name"],
#             last_name = validated_data["last_name"],
#         )

#         user.set_password(validated_data["password"])
#         user.save()

#         return user

# class UserViewSet(viewsets.ModelViewSet):

#     queryset = User.objects.all()
#     serializer_class = UserSerializer