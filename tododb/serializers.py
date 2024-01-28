from rest_framework import serializers 
from . models import Punch, Punchlist

class PunchSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Punch
        fields = ['id','checked','detail', 'punchlist_list']

class PunchListSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Punchlist
        fields = ['id','name_of_punchlist']