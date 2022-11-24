from django.contrib.auth.models import Group
from django.forms import ModelMultipleChoiceField
from django.utils.translation import gettext_lazy as _

from one.components.widgets import ModelSelectTwoMultiple


def quick_add_group_field():
    return ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
        label=_("Groups"),
        help_text=_("Select a group to add to the user"),
        widget=ModelSelectTwoMultiple(
            {
                "create_url": "auth:group-create",
                "update_url": "auth:group-update",
                "default_value": "0000",
            }
        ),
    )
