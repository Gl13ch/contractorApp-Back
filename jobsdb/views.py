from rest_framework import generics
from .serializers import JobSerializers, AddressSerializer
from .models import Job, Address

# Create your views here.
class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all().order_by('id')
    serializer_class = JobSerializers

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all().order_by('id')
    serializer_class = JobSerializers

class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all().order_by('id')
    serializer_class = AddressSerializer

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all().order_by('id')
    serializer_class = AddressSerializer