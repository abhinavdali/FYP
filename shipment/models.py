from django.conf import settings
from django.db import models
from accounts.models import CustomerUser, User

# Create your models here.

class Ship(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    of_type = models.CharField(max_length=100)
    weight = models.IntegerField()
    size = models.IntegerField()
    price = models.IntegerField()
    receiver = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)



