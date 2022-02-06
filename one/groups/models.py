from django.contrib.auth.models import Group
from django.db.models import CASCADE, CharField, Model, OneToOneField
from django.utils.translation import gettext_lazy as _

from one.components.constants import CLASS_COLOR, CLASS_DARK


class GroupProfile(Model):
    """
    Profile for Role/Group

    group: OneToOneField, Specific group
    color: CharField, Color of group
    """

    group = OneToOneField(Group, on_delete=CASCADE)
    color = CharField(
        _("Color of group"), max_length=7, choices=CLASS_COLOR, default=CLASS_DARK
    )

    @property
    def display_as_html(self):
        """Get level html"""
        return f"""
                <span class='badge badge-{self.color} fw-bolder fs-8 px-2 py-1
                '>{self.group.name}</span>
            """
