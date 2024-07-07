import uuid
from django.db import models

from emr.models.generic import Person
from emr.models.business import Facility
from emr.models.billing import CareLevel

class Visit(models.Model):
    id = models.UUIDField(default=uuid.uuid4(),primary_key=True)
    person = models.ForeignKey(Person,on_delete=models.CASCADE,related_name='admissions')
    facility = models.ForeignKey(Facility,on_delete=models.CASCADE,related_name='admissions')
    admission_date = models.DateTimeField()
    discharge_date = models.DateTimeField(null=True)
    diagnosis = models.JSONField(default=[])

    def __str__(self):
        return self.id
    
class LevelOfCare(models.Model):
    id = models.UUIDField(default=uuid.uuid4(),primary_key=True)
    service = models.ForeignKey(CareLevel,on_delete=models.CASCADE,related_name="locs")
    visit = models.ForeignKey(Visit,on_delete=models.CASCADE,related_name="locs")
    start_date = models.DateField()
    end_date = models.DateField(null=True)

class Authorization(models.Model):
    id = models.UUIDField(default=uuid.uuid4(),primary_key=True)
    visit = models.ForeignKey(Visit,on_delete=models.CASCADE,related_name="authorizations")
    authorization_code = models.CharField(max_length=200)
    units = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    



