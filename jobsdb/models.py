from django.db import models
from users.models import User, Address

# Create your models here.
class Job(models.Model):
    start_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=False)
    description = models.TextField()
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)



