
import email
from rest_framework import serializers, viewsets
from django.contrib.auth.models import User

MIN_LENGTH = 8
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("__all__")

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only = True,
        min_length = MIN_LENGTH,
        error_messages = {
            "min_length":"Password must be longer than {MIN_LENGTH} characters."
        }
    )

    confirm_password = serializers.CharField(
        write_only = True,
        min_length = MIN_LENGTH,
        error_messages = {
            "min_length":"Password must be longer than {MIN_LENGTH} characters."
        }
    )

    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name','password','confirm_password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Password does not match.")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )

        user.set_password(validated_data["password"])
        user.save()

        return user

