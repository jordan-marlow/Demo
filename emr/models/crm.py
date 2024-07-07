from django.db import models
import uuid

from emr.models.generic import Person

class LeadStatus(models.Model):
    name = models.CharField(max_length=100,unique=True)
    created_on = models.DateField(auto_now_add=True,editable=False)
    modified_on = models.DateField(auto_now=True,editable=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class LeadSource(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name
    
class OpportunityStage(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    # Add more fields as necessary

    def __str__(self):
        return self.name


class Lead(models.Model):
    id = models.UUIDField(default=uuid.uuid4(),primary_key=True)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)

    status = models.ForeignKey(LeadStatus,on_delete=models.SET_NULL,null=True,related_name="leads")
    source = models.ForeignKey(LeadSource,on_delete=models.SET_NULL,null=True,related_name="leads")
    notes = models.TextField(blank=True, null=True)
    # Other lead-specific fields...

    def __str__(self):
        return f"{self.person.first_name} {self.person.last_name}"


class Opportunity(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    stage = models.ForeignKey(OpportunityStage,on_delete=models.SET_NULL,null=True,related_name="opportunities")
    close_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title