from django.urls import path

from measurement.views import ListCreateSensorsView, CreateMeasurementView, RetrieveUpdateSensor

urlpatterns = [
    path('sensors/', ListCreateSensorsView.as_view()),
    path('measurements/', CreateMeasurementView.as_view()),
    path('measurements/<pk>/', RetrieveUpdateSensor.as_view())
]
