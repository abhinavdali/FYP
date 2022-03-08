from django.db import models

from accounts.models import CustomerUser

# Create your models here.

class Ship(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    of_type = models.CharField(max_length=100)
    weight = models.IntegerField()
    size = models.IntegerField()
    price = models.IntegerField()



