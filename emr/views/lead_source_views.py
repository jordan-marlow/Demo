from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from emr.models.crm import LeadSource

class LeadSourceListView(ListView):
    model = LeadSource
    template_name = 'leadsource_list.html'
    context_object_name = 'lead_statuses'

    def get_template_names(self):
        if self.request.htmx:
            return ["partials/leadsource_list_partial.html"]
        return ["leadsource_list.html"]

class CreateLeadSource(CreateView):
    model = LeadSource
    template_name = 'partials/leadsource_form.html'
    success_url = reverse_lazy("emr:leadsource_list")
    fields = "__all__"

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.htmx:
            return render(self.request, "partials/leadsource_list_partial.html", {"object_list": self.model.objects.all()})
        return response

class UpdateLeadSource(UpdateView):
    model = LeadSource
    template_name = 'partials/leadsource_form.html'
    success_url = reverse_lazy("emr:leadsource_list")
    fields = "__all__"

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.htmx:
            return render(self.request, "partials/leadsource_list_partial.html", {"object_list": self.model.objects.all()})
        return response

class DeleteLeadSource(DeleteView):
    model = LeadSource
    template_name = 'partials/leadsource_confirm_delete.html'
    success_url = reverse_lazy("emr:leadsource_list")

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        if self.request.htmx:
            return render(self.request, "partials/leadsource_list_partial.html", {"object_list": self.model.objects.all()})
        return response
