import requests
import random
import time

while True:

    data = {
        "car": 1,
        "speed": random.randint(40,120),
        "engine_temp": random.randint(70,110),
        "battery_health": random.randint(70,100)
    }
    data = {
        "car": 2,
        "speed": random.randint(30,110),
        "engine_temp": random.randint(60,100),
        "battery_health": random.randint(80,130)
    }

    response = requests.post(
        "http://127.0.0.1:8000/api/telemetry/",
        json=data
    )

    print("Telemetry sent:", data)
    print("Server response:", response.json())

    time.sleep(5)