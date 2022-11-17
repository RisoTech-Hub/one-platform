from uuid import uuid4

from django.db.models import CASCADE, CharField, ForeignKey, JSONField, Model, UUIDField
from django.utils.translation import gettext_lazy as _


class Menu(Model):
    POSITION_TOP = "top"
    POSITION_BOTTOM = "bottom"
    POSITION_SIDEBAR = "sidebar"

    POSITION_CHOICES = (
        (POSITION_TOP, _("Top")),
        (POSITION_BOTTOM, _("Bottom")),
        (POSITION_SIDEBAR, _("Sidebar")),
    )

    id = UUIDField(_("ID"), primary_key=True, default=uuid4, editable=False)
    name = CharField(_("Name of Menu"), blank=False, null=False, max_length=255)
    render = JSONField(_("Render Json"), blank=True, null=True, default=dict)
    position = CharField(
        _("Position"),
        blank=False,
        null=False,
        max_length=255,
        choices=POSITION_CHOICES,
        default=POSITION_SIDEBAR,
    )

    class Meta:
        verbose_name = _("Menu")
        verbose_name_plural = _("Menus")

    def __str__(self):
        return self.name


class MenuItem(Model):
    TYPE_CHOICE_LINK = "link"
    TYPE_CHOICE_ACCORDION = "accordion"
    TYPE_CHOICE_SECTION = "section"
    TYPE_CHOICES = (
        (TYPE_CHOICE_LINK, _("Link")),
        (TYPE_CHOICE_ACCORDION, _("Accordion")),
        (TYPE_CHOICE_SECTION, _("Section")),
    )

    id = UUIDField(_("Item ID"), primary_key=True, default=uuid4, editable=False)
    menu = ForeignKey(Menu, on_delete=CASCADE, related_name="items")
    type = CharField(
        _("Type of Item"), blank=False, null=False, max_length=10, choices=TYPE_CHOICES
    )
    label = CharField(_("Label of Item"), blank=False, null=False, max_length=255)
    link = CharField(_("Link of Item"), blank=True, null=True, max_length=255)
    icon = CharField(_("Icon of Item"), blank=True, null=True, max_length=255)
    unique_code = CharField(
        _("Unique Code of Item"), blank=True, null=True, max_length=255
    )

    class Meta:
        verbose_name = _("Menu Item")
        verbose_name_plural = _("Menu Items")

    def __str__(self):
        return f"{self.menu} {self.label}"
