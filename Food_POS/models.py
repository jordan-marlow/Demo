from django.db import models
import uuid

# Create your models here.

class Ingredient(models.Model):
    id = models.UUIDField(default=uuid.uuid4(),primary_key=True)
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10,decimal_places=2)
    units = models.CharField(max_length=10)

class Item(models.Model):
    id = models.UUIDField(default=uuid.uuid4(),primary_key=True)
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)
    price = models.DecimalField(max_digits=10,decimal_places=2)

class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4(),primary_key=True)
    items = models.ManyToManyField(Item)
    include_tax = models.BooleanField(default=True)

