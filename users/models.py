from django.db import models

# Create your models here.
class Address(models.Model):
    street_line1 = models.CharField(max_length = 100, blank = True)
    street_line2 = models.CharField(max_length = 100, blank = True)
    zip = models.CharField(max_length = 5)
    city = models.CharField(max_length = 50, blank = False)
    state = models.CharField(max_length = 40, blank = True)

class User(models.Model):
    email = models.CharField(max_length=254, unique=True, blank=True, null=True)
    password = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)