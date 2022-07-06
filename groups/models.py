from uuid import uuid4
from django.db import models

# Create your models here.


class Groups(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    breed = models.CharField(max_length=20)
