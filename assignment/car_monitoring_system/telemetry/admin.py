from django.contrib import admin
from .models import Car, TelemetryData, Update

admin.site.register(Car)
admin.site.register(TelemetryData)
admin.site.register(Update)