from django.urls import path

from .views import lead_status_views

app_name = "emr"

urlpatterns = [
    path('leadstatus/', lead_status_views.LeadStatusListView.as_view(), name="leadstatus_list"),
    path('leadstatus/create/', lead_status_views.CreateLeadStatus.as_view(), name="leadstatus_create"),
    path('leadstatus/update/<int:pk>/', lead_status_views.UpdateLeadStatus.as_view(), name="leadstatus_update"),
    path('leadstatus/delete/<int:pk>/', lead_status_views.DeleteLeadStatus.as_view(), name="leadstatus_delete"),
]
