from django.db import models


class Car(models.Model):

    vin = models.CharField(max_length=50, unique=True)
    model = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)

    def __str__(self):
        return self.vin


class TelemetryData(models.Model):

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    speed = models.FloatField()
    engine_temp = models.FloatField()
    battery_health = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)


class Update(models.Model):

    UPDATE_TYPE = (
        ("critical", "Critical"),
        ("non_critical", "Non Critical"),
    )

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    version = models.CharField(max_length=20)

    update_type = models.CharField(max_length=20, choices=UPDATE_TYPE)

    status = models.CharField(max_length=20, default="pending")

    created_at = models.DateTimeField(auto_now_add=True)