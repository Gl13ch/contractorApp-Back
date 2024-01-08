from rest_framework import generics
from .serializers import ToDoSerializers
from .models import ToDo

# Create your views here.
class ToDoList(generics.ListCreateAPIView):
    queryset = ToDo.objects.all().order_by('id')
    serializer_class = ToDoSerializers

class ToDoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all().order_by('id')
    serializer_class = ToDoSerializers
