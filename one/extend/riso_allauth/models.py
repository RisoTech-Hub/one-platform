from uuid import uuid4

from django.conf import settings
from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKey,
    Model,
    TextField,
    UUIDField,
)
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .constants import ALLAUTH_TEMPLATES


class AllauthTemplate(Model):
    """
    Email template for reuse

    code: CharField, Specific code for core app
    subject: CharField, Email title
    is_protected: BooleanField, can delete or not
    content: TextField, html content
    """

    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    time_created = DateTimeField(
        verbose_name=_("Created on"), auto_now_add=True, null=True
    )
    time_modified = DateTimeField(
        verbose_name=_("Last modified on"), auto_now=True, null=True
    )
    creator = ForeignKey(
        "users.User",
        verbose_name=_("Created by"),
        related_name="%(app_label)s_%(class)s_creator",
        null=True,
        blank=True,
        on_delete=CASCADE,
    )
    last_modified_by = ForeignKey(
        "users.User",
        verbose_name="Last modified by",
        related_name="%(app_label)s_%(class)s_last_modified_by",
        null=True,
        blank=True,
        on_delete=CASCADE,
    )

    language = CharField(
        _("Language"),
        max_length=2,
        blank=True,
        null=True,
        editable=False,
        choices=settings.LANGUAGES,
        default=settings.VIETNAMESE,
    )
    code = CharField(
        _("Specific code for core app"),
        max_length=50,
        blank=True,
        null=True,
        editable=False,
        choices=ALLAUTH_TEMPLATES,
    )
    subject = CharField(_("Subject of email"), max_length=1000, blank=True, null=True)
    is_protected = BooleanField(_("Is protected"), default=False)
    content = TextField(_("Html content"))

    class Meta:
        permissions = [
            ("list_allauthtemplate", "Can list allauth email template"),
        ]
        unique_together = (
            "code",
            "language",
        )

    def save(self, *args, **kwargs):
        if not self.time_created:
            self.time_created = timezone.now()

        self.time_modified = timezone.now()
        return super().save(*args, **kwargs)  # noqa

    @property
    def language_verbose(self):
        return dict(settings.LANGUAGES)[self.language]

    @property
    def code_verbose(self):
        return dict(ALLAUTH_TEMPLATES)[self.code]
