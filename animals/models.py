from uuid import uuid4
from django.db import models

# Create your models here.

class Animals(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=20)
    weight = models.FloatField()
    height = models.IntegerField()
    years_old = models.IntegerField()
    favorite_toy = models.CharField(max_length=20)
    friendly = models.BooleanField()

    owner = models.ForeignKey(to="users.Users", on_delete=models.CASCADE, related_name="animals")
    breed = models.ForeignKey(to="breeds.Breeds", on_delete=models.CASCADE ,related_name="animals" ) 

    # Preciso colocar related_name em breed?
