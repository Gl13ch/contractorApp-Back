from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=254, unique=True)
    password = models.CharField(max_length=100)
    phone = models.IntegerField()
    first_name = models.CharField(max_length=50,blank=True, null=True)
    last_name = models.CharField(max_length=50,blank=True, null=True)
    is_admin = models.BooleanField(default=False)