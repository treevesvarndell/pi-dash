from django.db import models


class TrainDeparture(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    eta = models.DateTimeField()
    destination = models.CharField(max_length=50)
    station = models.CharField(max_length=50)
