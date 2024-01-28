from rest_framework import generics
from .serializers import PunchSerializers, PunchListSerializers
from .models import Punch, Punchlist

# Create your views here.
class PunchList(generics.ListCreateAPIView):
    queryset = Punch.objects.all().order_by('id')
    serializer_class = PunchSerializers

class PunchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Punch.objects.all().order_by('id')
    serializer_class = PunchSerializers
    
class PunchListList(generics.ListCreateAPIView):
    queryset = Punchlist.objects.all().order_by('id')
    serializer_class = PunchListSerializers

class PunchListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Punchlist.objects.all().order_by('id')
    serializer_class = PunchListSerializers




