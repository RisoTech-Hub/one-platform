from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import UpdateView

from one.components.views import CreateView, FormMixin, ListView, SuccessMessageMixin
from one.contrib.auth.contexts.actions import (
    get_core_group_add,
    get_core_group_quick_add,
)
from one.contrib.auth.contexts.api.serializers import GroupSerializer
from one.contrib.auth.contexts.filters import GroupFilter
from one.contrib.auth.contexts.forms import ContextForm, GroupForm


class GroupCreateView(LoginRequiredMixin, SuccessMessageMixin, FormMixin, CreateView):
    model = Group

    form_class = GroupForm
    serializer_class = GroupSerializer
    success_message = _("Group created successfully")

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["app_name"] = _("Group")
        kwargs["page_title"] = _("Group Create")
        kwargs["page_breadcrumb"] = [
            {"name": _("Groups"), "url": reverse("auth:group-list")},
        ]

        kwargs["form_title"] = _("Group Form")
        kwargs["nested_forms"] = [
            {
                "form": ContextForm(),
                "title": _("Extend information"),
            }
        ]
        return kwargs

    def get_success_url(self):  # noqa
        if self.object:
            return reverse("auth:group-update", kwargs={"pk": self.object.pk})
        return reverse("auth:group-list")

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            context_form = ContextForm(self.request.POST, self.request.FILES)
            if context_form.is_valid():
                response = self.form_valid(form)
                context_form = ContextForm(
                    self.request.POST, self.request.FILES, instance=self.object.context
                )
                context_form.save()
                return response
            self.object = None  # noqa
            self.add_error_messages(context_form)
        return self.form_invalid(form)


group_create_view = GroupCreateView.as_view()


class GroupListView(LoginRequiredMixin, ListView):
    template_name = "app/list.html"
    model = Group

    filter_class = GroupFilter

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["app_name"] = _("Group")
        kwargs["page_title"] = _("Group List")
        kwargs["actions"] = [get_core_group_add(), get_core_group_quick_add()]
        kwargs["urls"] = {
            "update": "auth:group-update",
        }
        kwargs["api_urls"] = {
            "list": "api:group-list",
            "delete": "api:group-delete",
        }
        return kwargs


group_list_view = GroupListView.as_view()


class GroupUpdateView(LoginRequiredMixin, SuccessMessageMixin, FormMixin, UpdateView):
    template_name = "app/update.html"
    model = Group

    form_class = GroupForm
    serializer_class = GroupSerializer
    success_message = _("Group successfully updated")

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["app_name"] = _("Group")
        kwargs["page_title"] = _("Group Update")
        kwargs["page_breadcrumb"] = [
            {"name": _("Groups"), "url": reverse("auth:group-list")},
        ]

        kwargs["form_title"] = _("Group Update")

        if self.request.method == "POST":
            context_form = ContextForm(
                self.request.POST, self.request.FILES, instance=self.object.context
            )
        else:
            context_form = ContextForm(instance=self.object.context)
        kwargs["nested_forms"] = [
            {
                "form": context_form,
                "title": _("Extend information"),
                "hidden_fields": [],
            }
        ]
        return kwargs

    def get_success_url(self):  # noqa
        return reverse("auth:group-list")

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        self.object = self.get_object()  # noqa
        context_form = ContextForm(
            self.request.POST, self.request.FILES, instance=self.object.context
        )
        form = self.get_form()
        if form.is_valid():
            if context_form.is_valid():
                self.form_valid(context_form, is_nested=True)
                return self.form_valid(form)
            self.add_error_messages(context_form)
        return self.form_invalid(form)


group_update_view = GroupUpdateView.as_view()
