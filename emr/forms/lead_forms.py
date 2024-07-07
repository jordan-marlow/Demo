from django.forms import ModelForm

from emr.models.crm import LeadStatus, LeadSource, Lead

class LeadStatusCreateForm(ModelForm):
    class Meta:
        model = LeadStatus
        fields = "__all__"

