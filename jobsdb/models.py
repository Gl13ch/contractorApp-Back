from django.db import models

# Create your models here.
class Address(models.Model):
    street_line1 = models.CharField(max_length = 100, blank = True)
    street_line2 = models.CharField(max_length = 100, blank = True)
    zip = models.CharField(max_length = 5)
    city = models.CharField(max_length = 50, blank = False)
    state = models.CharField(max_length = 40, blank = True)

class Client(models.Model):
    email = models.CharField(max_length=254)
    phone = models.IntegerField()
    first_name = models.CharField(max_length=50,blank=True, null=True)
    last_name = models.CharField(max_length=50,blank=True, null=True)

class Job(models.Model):
    start_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=False)
    description = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)

# ONJOBCREATE make dummy user


