import random
from .models import TelemetryData, Update


def process_telemetry(telemetry_id):
    
    telemetry = TelemetryData.objects.get(id=telemetry_id)

    # Monitoring logic
    if telemetry.engine_temp > 100:
        severity = "critical"
    else:
        severity = "non_critical"

    print("Monitoring Result:", severity)

    if severity == "critical":

        Update.objects.create(
            car=telemetry.car,
            version="v2.1",
            update_type="critical",
            status="pending"
        )

        print("Update Created: Critical Update")

    else:

        Update.objects.create(
            car=telemetry.car,
            version="v2.1",
            update_type="non_critical",
            status="scheduled"
        )

        print("Update Created: Non Critical Update")

def evaluate_update(response):

    if response["severity"] == "critical":
        return "update_now"

    return "schedule_later"