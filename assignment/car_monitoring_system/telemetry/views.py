from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TelemetrySerializer , UpdateSerializer
from .tasks import process_telemetry
from .models import Update

class TelemetryView(APIView):

    def post(self, request):

        serializer = TelemetrySerializer(data=request.data)

        if serializer.is_valid():

            telemetry = serializer.save()

            process_telemetry(telemetry.id)

            return Response({"message": "Telemetry received"})

        return Response(serializer.errors)
    
    
    
class UpdateView(APIView):
    
    def get(self, request):

        car_id = request.GET.get("car")

        updates = Update.objects.filter(car_id=car_id)

        serializer = UpdateSerializer(updates, many=True)

        return Response(serializer.data)    