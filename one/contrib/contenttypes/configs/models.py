from django.contrib.contenttypes.models import ContentType
from django.db.models import CASCADE, Model, OneToOneField
from django.utils.translation import gettext_lazy as _


class Config(Model):
    """Config model is OneToOne related to Site model."""

    contenttype = OneToOneField(
        ContentType,
        on_delete=CASCADE,
        primary_key=True,
        related_name="config",
        verbose_name=_("Content Type"),
    )

    class Meta:
        app_label = "contenttypes"
        verbose_name = _("Content Type")
        verbose_name_plural = _("Content Types")
        db_table = "django_content_type_config"

    def __str__(self):
        return f"{self.contenttype.app_label} {self.contenttype.model}"
