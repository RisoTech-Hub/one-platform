"""Declare filters for models."""
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django_filters import ChoiceFilter, FilterSet, NumberFilter

from one.components.widgets import BootstrapInput, SelectTwo
from one.extend.riso_allauth.models import AllauthTemplate


class AllauthTemplateFilter(FilterSet):
    id = NumberFilter(
        field_name="id",
        label=_("ID"),
        widget=BootstrapInput(
            {"placeholder": _("ID"), "data-kt-table-filter-col": "id"}
        ),
    )
    language = ChoiceFilter(
        field_name="language",
        label=_("Language"),
        choices=settings.LANGUAGES,
        widget=SelectTwo(
            {
                "data-kt-table-filter-col": "language",
            }
        ),
    )

    class Meta:
        model = AllauthTemplate
        fields = ["id"]
