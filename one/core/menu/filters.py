"""Declare filters for models."""
from django.utils.translation import gettext_lazy as _
from django_filters import CharFilter, FilterSet, NumberFilter

from one.components.widgets import BootstrapInput
from one.core.menu.models import Menu


class MenuFilter(FilterSet):
    id = NumberFilter(
        field_name="id",
        label=_("ID"),
        widget=BootstrapInput(
            {"placeholder": _("ID"), "data-kt-table-filter-col": "id"}
        ),
    )
    name = CharFilter(
        field_name="name",
        label=_("Name"),
        widget=BootstrapInput(
            {"placeholder": _("Name"), "data-kt-table-filter-col": "name"}
        ),
    )

    class Meta:
        model = Menu
        fields = ["id", "name"]
