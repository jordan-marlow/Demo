import uuid
from django.db import models


class Entity(models.Model):
    id = models.UUIDField(default=uuid.uuid4(),primary_key=True)
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Facility(models.Model):
    id = models.UUIDField(default=uuid.uuid4(),primary_key=True)
    entity = models.ForeignKey(Entity,on_delete=models.CASCADE,related_name="facilities")
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
