from rest_framework import serializers
from .models import TelemetryData, Update


class TelemetrySerializer(serializers.ModelSerializer):

    class Meta:
        model = TelemetryData
        fields = "__all__"


class UpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Update
        fields = "__all__"