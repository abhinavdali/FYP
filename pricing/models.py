from django.db import models

# Create your models here.

TYPE_CHOICES = (
    ('Document','DOCUMENT'),
    ('parcel', 'PARCEL'),
)


class Pricing(models.Model):
    typeOf = models.CharField(max_length=100, choices=TYPE_CHOICES, default='document')
    weight = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    price = models.CharField(max_length=100)