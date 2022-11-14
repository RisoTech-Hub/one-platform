from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, UpdateView

from one.components.views import FormMixin, SuccessMessageMixin

from .api.serializers import FieldSchemaSerializer
from .forms import FieldFormSet, FieldSchemaForm
from .models import FieldSchema


class FieldSchemaCreateView(
    LoginRequiredMixin, SuccessMessageMixin, FormMixin, CreateView
):
    template_name = "app/create.html"
    model = FieldSchema

    form_class = FieldSchemaForm
    serializer_class = FieldSchemaSerializer

    success_message = _("Field Schema created successfully")

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["page_title"] = _("Field Schema Create")
        kwargs["page_breadcrumb"] = [
            {"name": _("Home"), "url": reverse("home")},
            {"name": _("Field Schema Create"), "url": ""},
        ]

        kwargs["form_title"] = _("Field Schema Create")
        kwargs["hidden_fields"] = ["render"]
        if self.request.POST:
            field_formset = FieldFormSet(self.request.POST, prefix="items")
        else:
            field_formset = FieldFormSet(prefix="items")

        kwargs["formsets"] = [
            {
                "formset": field_formset,
                "title": _("Field Schema Items"),
                "hidden_fields": ["attrs"],
                "prefix": "items",
            }
        ]
        return kwargs

    def get_success_url(self):  # noqa
        return reverse("fieldschema:fieldschema-list")

    def get_template_names(self):
        if self.is_popup:
            return ["dynamic/field-schema-form.html"]
        return super().get_template_names()  # noqa


field_schema_create_view = FieldSchemaCreateView.as_view()


class FieldSchemaUpdateView(
    LoginRequiredMixin, SuccessMessageMixin, FormMixin, UpdateView
):
    template_name = "app/update.html"
    model = FieldSchema

    form_class = FieldSchemaForm
    serializer_class = FieldSchemaSerializer
    success_message = _("Field Schema successfully updated")

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["page_title"] = _("Field Schema Update")
        kwargs["page_breadcrumb"] = [
            {"name": _("Home"), "url": reverse("home")},
            {"name": _("Field Schema Update"), "url": ""},
        ]

        kwargs["form_title"] = _("Field Schema Update")
        return kwargs

    def get_success_url(self):  # noqa
        return reverse("fieldschema:fieldschema-list")

    def get_template_names(self):
        if self.is_popup:
            return ["dynamic/field-schema-form.html"]
        return super().get_template_names()  # noqa


field_schema_update_view = FieldSchemaUpdateView.as_view()
