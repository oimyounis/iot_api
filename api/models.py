from django.db import models
from psqlextra.models import PostgresModel


class Device(PostgresModel):
    id = models.CharField(primary_key=True, max_length=255)
    model = models.CharField(max_length=255, null=True)
    online = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Temperature(PostgresModel):
    time = models.DateTimeField(primary_key=True, auto_now_add=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='temps')
    value = models.FloatField()


class Pressure(PostgresModel):
    time = models.DateTimeField(primary_key=True, auto_now_add=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='bps')
    value = models.FloatField()
