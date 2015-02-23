from django.db import models


class TrainDeparture(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    direction = models.CharField(max_length=4)
    eta = models.DateTimeField(default=None, blank=True, null=True)
    destination = models.CharField(max_length=50)
    station = models.CharField(max_length=50)
