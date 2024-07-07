from django.db import models
import uuid

class Person(models.Model):
    #This will contain all of the Hippa info so to not leak information
    id = models.UUIDField(default=uuid.uuid4(),primary_key=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name
    
    def full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}".replace("  "," ").strip()
    
    def name(self):
        return f"{self.first_name} {self.last_name}"