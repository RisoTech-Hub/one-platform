"""Declare filters for models."""
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django_filters import CharFilter, ChoiceFilter, FilterSet, NumberFilter

from one.components.widgets import BootstrapInput, FloatingLabelSelectTwo
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
    language = ChoiceFilter(
        field_name="language",
        label=_("Language"),
        choices=settings.LANGUAGES,
        widget=FloatingLabelSelectTwo({"data-kt-table-filter-col": "language"}),
    )

    class Meta:
        model = Menu
        fields = ["id", "name", "language"]
