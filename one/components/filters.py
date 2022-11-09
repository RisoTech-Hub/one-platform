from django.utils.translation import gettext_lazy as _
from django_filters import CharFilter, FilterSet

from one.components.widgets import BootstrapInput


class DynamicFilter(FilterSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = kwargs.get("request")

    # for item in extra_field_list:
    #     self.filters[f"extra_field_{item.field.field_code}"] = CharFilter(
    #         field_name=f"extra_fields__{item.field.field_code}",
    #         lookup_expr="icontains",
    #         label=item.field.field_name,
    #         widget=FormClassInput(),
    #     )


class SEOFilter(FilterSet):
    title = CharFilter(
        field_name="title",
        lookup_expr="icontains",
        label=_("Title"),
        widget=BootstrapInput(
            {"placeholder": _("Title"), "data-kt-table-filter-col": "title"}
        ),
    )

    class Meta:
        fields = ["title"]
