#Serializers basically used to convert data to python which can then be redered into JSON
from rest_framework import serializers 
from . models import Testing

class TestSerializers(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta: 
        model = Testing # tell django which model to use
        fields = ['id','name', 'number'] # tell django which fields to include