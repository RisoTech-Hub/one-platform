from uuid import uuid4

from django.db.models import BooleanField, CharField, Model, TextField, UUIDField
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
        verbose_name = _("Allauth Template")
        verbose_name_plural = _("Allauth Templates")

    @property
    def code_verbose(self):
        return dict(ALLAUTH_TEMPLATES)[self.code]
