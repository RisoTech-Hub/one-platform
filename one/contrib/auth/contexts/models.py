from django.contrib.auth.models import Group
from django.db.models import CASCADE, ImageField, Model, OneToOneField
from django.utils.translation import gettext_lazy as _

from .utils import group_context_images_directory_path


class Context(Model):
    """Setting model is OneToOne related to Site model."""

    group = OneToOneField(
        Group,
        on_delete=CASCADE,
        primary_key=True,
        related_name="context",
        verbose_name="group",
    )

    avatar = ImageField(
        _("Avatar of group"),
        blank=True,
        null=True,
        upload_to=group_context_images_directory_path,
    )

    class Meta:
        app_label = "auth"
        verbose_name = _("Context")
        verbose_name_plural = _("Contexts")
        db_table = "auth_group_context"

    def __str__(self):
        return self.group.name
