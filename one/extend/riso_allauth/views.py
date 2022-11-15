from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import UpdateView

from one.components.views import FormMixin, ListView, SuccessMessageMixin

from .api.serializers import TemplateSerializer
from .filters import AllauthTemplateFilter
from .forms import TemplateForm
from .models import AllauthTemplate


class TemplateListView(LoginRequiredMixin, ListView):
    template_name = "app/list.html"
    model = AllauthTemplate

    table_exclude_fields = [
        "id",
        "creator",
        "time_created",
        "time_modified",
        "last_modified_by",
        "content",
        "code",
        "is_protected",
    ]

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["page_title"] = _("Template List")
        kwargs["page_breadcrumb"] = [
            {"name": _("Home"), "url": reverse("home")},
            {"name": _("Templates"), "url": ""},
        ]

        kwargs["urls"] = {
            "update": "allauth:template-update",
        }

        kwargs["api_urls"] = {
            "list": "api:allauthtemplate-list",
            "delete": "api:allauthtemplate-delete",
        }
        kwargs["filter"] = AllauthTemplateFilter()
        kwargs["skip_popup"] = True
        return kwargs


template_list_view = TemplateListView.as_view()


class TemplateUpdateView(
    LoginRequiredMixin, SuccessMessageMixin, FormMixin, UpdateView
):
    template_name = "app/update.html"
    model = AllauthTemplate

    form_class = TemplateForm
    serializer_class = TemplateSerializer
    success_message = _("Template successfully updated")

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["page_title"] = _("Template Update")
        kwargs["page_breadcrumb"] = [
            {"name": _("Home"), "url": reverse("home")},
            {"name": _("Templates"), "url": reverse("allauth:template-list")},
            {"name": _("Template Update"), "url": ""},
        ]

        kwargs["form_title"] = _("Template Update")
        return kwargs

    def get_success_url(self):  # noqa
        return reverse("allauth:template-list")


template_update_view = TemplateUpdateView.as_view()
