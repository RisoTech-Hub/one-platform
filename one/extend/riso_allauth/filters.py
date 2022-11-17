"""Declare filters for models."""
from django.utils.translation import gettext_lazy as _
from django_filters import FilterSet, NumberFilter

from one.components.widgets import BootstrapInput
from one.extend.riso_allauth.models import AllauthTemplate


class AllauthTemplateFilter(FilterSet):
    id = NumberFilter(
        field_name="id",
        label=_("ID"),
        widget=BootstrapInput(
            {"placeholder": _("ID"), "data-kt-table-filter-col": "id"}
        ),
    )

    class Meta:
        model = AllauthTemplate
        fields = ["id"]
