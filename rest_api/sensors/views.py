from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from .models import Sensor
from .serializers import SensorDataSerializer
from rest_framework.permissions import IsAuthenticated
from .filters import SensorDataFilter

class StandardResultsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class SensorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all().order_by('id')
    serializer_class = SensorDataSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = SensorDataFilter
    ordering_fields = ['system', 'ph', 'temperature', 'tds', 'created_time']
    pagination_class = StandardResultsPagination

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Sensor.objects.filter(system__owner=self.request.user)

class SensorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDataSerializer
    permission_classes = [IsAuthenticated]