from rest_framework import generics
from .serializers import TestSerializers
from .models import Testing

# Create your views here.
class TestingList(generics.ListCreateAPIView):
    queryset = Testing.objects.all().order_by('number') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = TestSerializers # tell django what serializer to use

class TestingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Testing.objects.all().order_by('number')
    serializer_class = TestSerializers