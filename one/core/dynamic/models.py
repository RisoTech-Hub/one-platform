from uuid import uuid4

from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    ForeignKey,
    JSONField,
    Model,
    UUIDField,
)
from django.utils.translation import gettext_lazy as _

from one.core.dynamic.constants import FIELD_TYPE_CHARFIELD, FIELD_TYPE_CHOICES


class FieldSchema(Model):
    id = UUIDField(_("ID"), primary_key=True, default=uuid4, editable=False)
    name = CharField(_("Name of Schema"), blank=False, null=False, max_length=255)
    is_active = BooleanField(_("Is Active"), default=False)
    model = ForeignKey(
        "contenttypes.ContentType",
        on_delete=CASCADE,
        related_name="field_schemas",
        verbose_name=_("Content Type Model"),
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _("Field Schema")
        verbose_name_plural = _("Field Schemas")

    def __str__(self):
        return self.name

    def set_active(self):
        FieldSchema.objects.filter(model=self.model).update(is_active=False)
        self.is_active = True
        self.save()


class Field(Model):
    id = UUIDField(_("ID"), primary_key=True, default=uuid4, editable=False)
    schema = ForeignKey(FieldSchema, on_delete=CASCADE)
    name = CharField(_("Name of Field"), blank=False, null=False, max_length=255)
    type = CharField(
        _("Type of Field"),
        blank=False,
        null=False,
        max_length=50,
        choices=FIELD_TYPE_CHOICES,
        default=FIELD_TYPE_CHARFIELD,
    )
    attrs = JSONField(_("Attributes"), blank=True, null=True, default=dict)

    class Meta:
        verbose_name = _("Field")
        verbose_name_plural = _("Fields")

    def __str__(self):
        return self.name

    @property
    def type_display(self):
        return dict(FIELD_TYPE_CHOICES)[self.type]
