
# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import Task
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .permissions import IsOwnerOrReadOnly


from .serializers import TaskSerializers
from rest_framework import permissions



class TaskApiList(ListAPIView):
    queryset = Task.objects.all()
    serializer_class  = TaskSerializers
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['title']
    search_fields = ['title']

class TaskApiCreate(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TaskApiRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    permission_classes = [IsOwnerOrReadOnly]
