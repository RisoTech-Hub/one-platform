from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.forms import ModelMultipleChoiceField
from django.utils.translation import gettext_lazy as _

from one.components.widgets import ModelSelectTwoMultiple

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    groups = ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
        label=_("Groups"),
        help_text=_("Select a group to add to the user"),
        widget=ModelSelectTwoMultiple(
            {
                "create_url": "auth:group-create",
                "update_url": "auth:group-update",
                "default_value": 999,
            }
        ),
    )

    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }
