from uuid import uuid4
from django.db import models

# Create your models here.

class Characteristic(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    weight = models.FloatField()
    height = models.IntegerField()
    years_old = models.IntegerField()
    favorite_toy = models.CharField(max_length=20)
    friendly = models.BooleanField()