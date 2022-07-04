from uuid import uuid4
from django.db import models

# Create your models here.

class Users(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    email = models.CharField(max_length=50)