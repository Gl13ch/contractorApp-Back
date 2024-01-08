from rest_framework import generics
from .serializers import JobSerializers
from .models import Job

# Create your views here.
class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all().order_by('id')
    serializer_class = JobSerializers

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all().order_by('id')
    serializer_class = JobSerializers