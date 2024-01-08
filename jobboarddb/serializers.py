from rest_framework import serializers 
from . models import JobBoard

class JobBoardSerializers(serializers.ModelSerializer):
    class Meta: 
        model = JobBoard
        fields = ['id','image','description','comments','owner']