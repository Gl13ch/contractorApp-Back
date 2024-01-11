from rest_framework import serializers 
from . models import Job, Address

class JobSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Job
        fields = ['id','start_date','active','description','client','address']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id','street_line1','street_line2','zip','city','state')