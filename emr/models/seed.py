from emr.models.crm import OpportunityStage, LeadSource, LeadStatus


def default_setup():
    default_opportunity_stages = ["Prospecting","Qualification","Proposal","Negotiation","Closed Won","Closed Lost"]
    OpportunityStage.objects.all().delete()
    for stage in default_opportunity_stages:
        obj = OpportunityStage.objects.create(name=stage)
        obj.save()

    default_lead_status = ["New","Contacted","Qualified","Converted","Unqualified"]
    LeadStatus.objects.all().delete()
    for status in default_lead_status:
        obj = LeadStatus.objects.create(name=status)
        obj.save()

    default_lead_sources = ["Referral","Website","Social Media","Email Campaign","Event","Advertising","Cold Call","Partnerships","Direct Mail"]
    for source in default_lead_sources:
        obj = LeadSource.objects.create(name=source)
        obj.save()


