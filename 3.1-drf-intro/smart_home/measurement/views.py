from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import MeasurementSerializer, SensorDetailSerializer


class ListCreateSensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class CreateMeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class RetrieveUpdateSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
