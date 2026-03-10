from django.urls import path
from .views import TelemetryView, UpdateView

urlpatterns = [
    path("telemetry/", TelemetryView.as_view()),
    path("update/", UpdateView.as_view()),
]