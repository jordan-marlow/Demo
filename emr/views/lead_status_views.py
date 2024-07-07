from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from emr.models.crm import LeadStatus

class LeadStatusListView(ListView):
    model = LeadStatus
    template_name = 'leadstatus_list.html'
    context_object_name = 'lead_statuses'

    def get_template_names(self):
        if self.request.htmx:
            return ["partials/leadstatus_list_partial.html"]
        return ["leadstatus_list.html"]

class CreateLeadStatus(CreateView):
    model = LeadStatus
    template_name = 'partials/leadstatus_form.html'
    success_url = reverse_lazy("emr:leadstatus_list")
    fields = "__all__"

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.htmx:
            return render(self.request, "partials/leadstatus_list_partial.html", {"object_list": self.model.objects.all()})
        return response

class UpdateLeadStatus(UpdateView):
    model = LeadStatus
    template_name = 'partials/leadstatus_form.html'
    success_url = reverse_lazy("emr:leadstatus_list")
    fields = "__all__"

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.htmx:
            return render(self.request, "partials/leadstatus_list_partial.html", {"object_list": self.model.objects.all()})
        return response

class DeleteLeadStatus(DeleteView):
    model = LeadStatus
    template_name = 'partials/leadstatus_confirm_delete.html'
    success_url = reverse_lazy("emr:leadstatus_list")

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        if self.request.htmx:
            return render(self.request, "partials/leadstatus_list_partial.html", {"object_list": self.model.objects.all()})
        return response
