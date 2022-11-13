from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import UpdateView

from one.cms.home.actions import get_cms_home_add, get_cms_home_quick_add
from one.cms.home.api.serializers import CMSHomeSerializer
from one.cms.home.filters import CMSHomeFilter
from one.cms.home.forms import CMSHomeForm
from one.cms.home.models import CMSHome
from one.components.views import CreateView, FormMixin, ListView, SuccessMessageMixin
from one.core.dynamic.actions import get_core_dynamic_field_schema_drawer


class CMSHomeCreateView(LoginRequiredMixin, SuccessMessageMixin, FormMixin, CreateView):
    template_name = "app/create.html"
    model = CMSHome

    form_class = CMSHomeForm
    serializer_class = CMSHomeSerializer

    success_message = _("CMS Home created successfully")

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["page_title"] = _("CMS Home Create")
        kwargs["page_breadcrumb"] = [
            {"name": _("Home"), "url": reverse("home")},
            {"name": _("CMS Homes"), "url": reverse("cmshome:cmshome-list")},
            {"name": _("CMS Home Create"), "url": ""},
        ]

        kwargs["form_title"] = _("CMS Home Form")
        return kwargs

    def get_success_url(self):  # noqa
        return reverse("cmshome:cmshome-list")


cmshome_create_view = CMSHomeCreateView.as_view()


class CMSHomeListView(LoginRequiredMixin, ListView):
    template_name = "app/list.html"
    model = CMSHome

    table_exclude_fields = [
        "id",
        "creator",
        "time_created",
        "time_modified",
        "last_modified_by",
        "dynamic",
    ]

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["page_title"] = _("CMS Home List")
        kwargs["page_breadcrumb"] = [
            {"name": _("Home"), "url": reverse("home")},
            {"name": _("CMS Homes"), "url": reverse("cmshome:cmshome-list")},
        ]
        kwargs["actions"] = [
            get_cms_home_add(),
            get_cms_home_quick_add(),
            get_core_dynamic_field_schema_drawer(),
        ]
        kwargs["urls"] = {
            "update": "cmshome:cmshome-update",
        }
        kwargs["api_urls"] = {
            "list": "api:cmshome-list",
            "delete": "api:cmshome-delete",
        }
        kwargs["filter"] = CMSHomeFilter()
        return kwargs


cmshome_list_view = CMSHomeListView.as_view()


class CMSHomeUpdateView(LoginRequiredMixin, SuccessMessageMixin, FormMixin, UpdateView):
    template_name = "app/update.html"
    model = CMSHome

    form_class = CMSHomeForm
    serializer_class = CMSHomeSerializer
    success_message = _("CMS Home successfully updated")

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["page_title"] = _("CMS Home Update")
        kwargs["page_breadcrumb"] = [
            {"name": _("Home"), "url": reverse("home")},
            {"name": _("CMS Homes"), "url": reverse("cmshome:cmshome-list")},
            {"name": _("CMS Home Update"), "url": ""},
        ]

        kwargs["form_title"] = _("CMS Home Update")
        return kwargs

    def get_success_url(self):  # noqa
        return reverse("cmshome:cmshome-list")


cmshome_update_view = CMSHomeUpdateView.as_view()
