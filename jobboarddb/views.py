from rest_framework import generics
from .serializers import JobBoardSerializers
from .models import JobBoard

# Create your views here.
class JobBoardList(generics.ListCreateAPIView):
    queryset = JobBoard.objects.all().order_by('id')
    serializer_class = JobBoardSerializers

class JobBoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobBoard.objects.all().order_by('id')
    serializer_class = JobBoardSerializers