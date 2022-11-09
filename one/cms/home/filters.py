from django.utils.translation import gettext_lazy as _
from django_filters import CharFilter, NumberFilter

from one.cms.home.models import CMSHome
from one.components.filters import DynamicFilter, SEOFilter
from one.components.widgets import BootstrapInput


class CMSHomeFilter(SEOFilter, DynamicFilter):
    id = NumberFilter(
        field_name="id",
        label=_("ID"),
        widget=BootstrapInput(
            {"placeholder": _("ID"), "data-kt-table-filter-col": "id"}
        ),
    )
    name = CharFilter(
        field_name="name",
        lookup_expr="contains",
        label=_("Name"),
        widget=BootstrapInput(
            {"placeholder": _("Name"), "data-kt-table-filter-col": "name"}
        ),
    )

    class Meta:
        model = CMSHome
        fields = ["id", "name"]
