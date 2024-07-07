from django.contrib import admin

# Register your models here.
from emr.models.crm import LeadStatus

myModels = [LeadStatus]  # iterable list
admin.site.register(myModels)