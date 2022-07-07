from uuid import uuid4
from django.db import models

# Create your models here.

class Animals(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=20)
    
    

    characteristic = models.OneToOneField(to="characteristic.Characteristic", on_delete=models.CASCADE, null=True)
    group = models.ForeignKey(to="groups.Groups", on_delete=models.CASCADE, null=True, related_name="animals" ) 

    # Preciso colocar related_name em breed?
