import uuid
from django.db import models

from emr.models.business import Facility
from emr.models.patient import Visit

class CareLevel(models.Model):
    id = models.UUIDField(default=uuid.uuid4())
    facility = models.ForeignKey(Facility,on_delete=models.CASCADE,related_name="care_levels")
    name = models.CharField(max_length=30)
    charge_amount = models.DecimalField(max_digits=10,decimal_places=2)
    admission_date_charge = models.BooleanField(default=True)
    discharge_date_charge = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Claim(models.Model):
    id = models.UUIDField(default=uuid.uuid4())
    admission = models.ForeignKey(Visit,null=True,blank=True)
    service_date = models.DateField()
    charge_amount = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    


    
