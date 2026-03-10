import requests


def call_monitoring_service(telemetry):

    payload = {
        "speed": telemetry.speed,
        "engine_temp": telemetry.engine_temp,
        "battery_health": telemetry.battery_health,
    }

    response = requests.post(
        "https://monitoring-service/api/check",
        json=payload
    )

    return response.json()


def evaluate_update(response):
    
    if response["severity"] == "critical":
        return "update_now"

    return "schedule_later"